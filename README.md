# Virtual Mental Health Project

## Project Overview  
The Virtual Mental Health Project leverages Artificial Intelligence and Natural Language Processing (NLP) to provide personalized and empathetic responses to users based on their emotional states. This project aims to create a supportive chatbot that can identify and respond to mental health challenges, offering tailored responses for various emotional states.

---

## Key Features  
- **Emotion Detection**  
  Utilizes sentiment analysis models to predict emotional states (e.g., negative, neutral, positive).  

- **Predefined Responses**  
  Responses are categorized based on sentiment:  
  - **Negative**: Extremely negative to slightly negative responses.  
  - **Neutral**: Balanced and emotionally steady responses.  
  - **Positive**: Encouraging and uplifting responses.  

- **Dynamic Sentiment Mapping**  
  Maps user input polarity values to predefined responses using a range of values between -1 and 1.  

- **Machine Learning Integration**  
  Employs an SVM (Support Vector Machine) model to classify mental health categories and provide response probabilities.  

- **Multi-category Response Support**  
  Supports six mental health categories:  
  - Anxiety  
  - Depression  
  - Stress  
  - Bipolar  
  - Suicidal  
  - Normal  
  - Personality-Disorder

---

## Technical Details  
- **Sentiment Analysis**  
  - Polarity values computed using NLTK, spaCy, and TextBlob.  
  - Predefined response ranges are mapped to sentiment scores for personalized feedback.  

- **Dataset**  
  - A  CSV dataset containing 3000 labeled sentences across six categories.  
  - Labels: Anxiety, Depression, Stress, Bipolar, Suicidal, Normal,Personality-Disorder.  

- **Response Logic**  
  - Responses stored in predefined arrays.  
  - Closest polarity values calculated using a helper function to dynamically determine the best-matched response.  

---

## Tools and Libraries  
- **Programming Language**: Python  
- **Libraries**:  
  - NLP: NLTK, spaCy, TextBlob  
  - Machine Learning: scikit-learn (SVM)  
  - Scaling: StandardScaler, MinMaxScaler  
  - Telegram Bot: `python-telegram-bot`  

---

## Future Enhancements  
- Real-time conversation analysis.  
- Advanced models for better emotional understanding.  
- Resources and links for mental health support.  
