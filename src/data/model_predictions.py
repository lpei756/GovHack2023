import pandas as pd
from transformers import BertTokenizer, BertForSequenceClassification, pipeline
from sklearn.metrics import accuracy_score, classification_report

# Loading the dataset
df = pd.read_csv('C:/Users/adamg/some_Gov_Hack/hand_scraped - Sheet1.csv')

# Loading pre-trained model and tokenizer
tokenizer = BertTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')
model = BertForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')
sentiment_pipeline = pipeline('sentiment-analysis', model=model, tokenizer=tokenizer)

# Function to predict sentiment based on the model's output
def get_sentiment(text):
    # Converting the input to string to ensure compatibility with the sentiment_pipeline
    text = str(text)

    # Extracting the numeric rating from the sentiment label
    label = sentiment_pipeline(text)[0]['label']
    rating = int(label.split()[0])
    
    if rating in [1, 2]:
        return 'negative'
    elif rating == 3:
        return 'neutral'
    else:
        return 'positive'


# Predicting sentiments for the dataset
df['Predicted_Sentiment'] = df['text'].apply(get_sentiment)



# Save the dataframe with the predictions to a new CSV file
df.to_csv('C:/Users/adamg/some_Gov_Hack/predicted_sentiments.csv', index=False)





