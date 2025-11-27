from textblob import TextBlob
import pandas as pd

def compute_sentiment(df):
    """
    Compute sentiment polarity for each 'Topic Quote' in df.
    Returns df with a new 'Sentiment' column.
    """
    df['Topic Quote'] = df['Topic Quote'].astype(str)
    df = df.dropna(subset=['Participant Number'])
    df['Participant Number'] = df['Participant Number'].astype(str)
    df['Sentiment'] = df['Topic Quote'].apply(lambda x: TextBlob(x).sentiment.polarity)
    return df

