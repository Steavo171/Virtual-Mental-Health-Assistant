from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from tenacity import retry, stop_after_attempt, wait_fixed
from responses import *
import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from generate import generate
import numpy as np
from polariser import *

TOKEN = ''  # Replace with your actual token from BotFather

data = pd.read_csv('datasets/pre_data.csv')     #loading the preprocessed data
X = data['text']
y = data['category']
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

svm_file=open('svm_model_probablity','rb')
svm_model=pickle.load(svm_file)
svm_file.close()

vectorizer = TfidfVectorizer(stop_words='english')
X_vectorized = vectorizer.fit_transform(X)


async def start(update: Update, context):
    user = update.message.from_user
    username = user.username
    context.user_data[username] = {
        "values": np.array([0.0] * 7),
        "length": 0, 
        "frequency":{
            "Anxiety":0,
            "Normal":0,
            "Depression":0,
            "Suicidal":0,
            "Stress":0,
            "Bipolar":0,
            "Personality disorder":0
        }
    }
    await update.message.reply_text("Hello! Welcome to the bot.")
    await update.message.reply_text("How can I help you?")


async def report(update: Update, context):
    user = update.message.from_user
    username = user.username
    first_name = user.first_name
    values = np.array(list(context.user_data[username]["frequency"].values()))
    total = sum(values)
    if total ==0:
        await update.message.reply_text("Report could not be generated due to lack of conversations.")
        return    
    avg_values = values/total
    generate(first_name,username,avg_values)
    await update.message._bot.send_document(chat_id=update.message.chat_id, document=open(f"PDF/{username}.pdf", 'rb'))
    await update.message.reply_text("Report sent successfully.")

async def echo(update: Update, context):
    user = update.message.from_user
    username = user.username
    user_input = update.message.text
    
    if user_input.lower() in "hello hi hey what's up? howdy  greetings welcome hiya yo  to see you how's it going? nice to meet you":
        await update.message.reply_text("Hello there !")
    
    # Analyze the user's input sentiment
    sentiment = get_polarity(user_input)
    response = get_response(sentiment)

    new_text = [user_input]
    
    new_text_vectorized = vectorizer.transform(new_text)
    category_probabilities = svm_model.predict_proba(new_text_vectorized)

    # print(data['category'].unique())
    #context.user_data["values"] = category_probabilities[0]

    print(category_probabilities[0])
    context.user_data[username]["values"] += category_probabilities[0]
    context.user_data[username]["length"] += 1
    svm_prediction = svm_model.predict(new_text_vectorized)
    svm_predicted_label = label_encoder.inverse_transform(svm_prediction)
    print(f"SVM Prediction: {svm_predicted_label[0]}")
    context.user_data[username]['frequency'][svm_predicted_label[0]] += 1
    print(context.user_data[username]['frequency'])
    await update.message.reply_text(response)

@retry(stop=stop_after_attempt(3), wait=wait_fixed(10))
def run_bot(application):
    application.run_polling()

def main():

    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("report", report))
    application.add_handler(MessageHandler(filters.TEXT, echo))

    run_bot(application)

if __name__ == "__main__":
    main()
