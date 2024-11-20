from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

import spacy
from spacytextblob.spacytextblob import SpacyTextBlob

from textblob import TextBlob

nltk.download('vader_lexicon')
nlp = spacy.load('en_core_web_sm')
nlp.add_pipe('spacytextblob')

def get_polarity(text):
    sia = SentimentIntensityAnalyzer()
    sentiment = sia.polarity_scores(text)["compound"]
    print(text , sentiment) 
    return sentiment
    
def get_polarity1(text):
    doc = nlp(text)
    polarity = doc._.blob.polarity
    print(text,polarity)
    return polarity