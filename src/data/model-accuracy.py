import pandas as pd
from transformers import BertTokenizer, BertForSequenceClassification, pipeline
from sklearn.metrics import accuracy_score, classification_report

# Load labeled data
df = pd.read_csv('C:/Users/adamg/some_Gov_Hack/train - Sheet1.csv')

# Load pre-trained model and tokenizer
tokenizer = BertTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')
model = BertForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')
sentiment_pipeline = pipeline('sentiment-analysis', model=model, tokenizer=tokenizer)

# Function to predict sentiment based on the model's output
def get_sentiment(text):
    # Convert the input to string to ensure compatibility with the sentiment_pipeline
    text = str(text)
    # Extract the numeric value from the sentiment label
    label = sentiment_pipeline(text)[0]['label']
    rating = int(label.split()[0])
    
    if rating in [1, 2]:
        return 'negative'
    elif rating == 3:
        return 'neutral'
    else:
        return 'positive'


# Predict sentiments for the dataset
df['Predicted_Sentiment'] = df['text'].apply(get_sentiment)

# Evaluate model's performance
accuracy = accuracy_score(df['sentiment'], df['Predicted_Sentiment'])
print(f"Accuracy: {accuracy:.2f}")

report = classification_report(df['sentiment'], df['Predicted_Sentiment'])
print(report)
