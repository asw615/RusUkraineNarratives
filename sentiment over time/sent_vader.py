# Import necessary libraries
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

# Instantiate a SentimentIntensityAnalyzer object
analyzer = SentimentIntensityAnalyzer()

# Load the text data into a pandas DataFrame
df = pd.read_csv('/Users/sorenmeiner/Library/CloudStorage/OneDrive-Aarhusuniversitet/CogComm exam/webscraper/csv_data/ukraine_df.csv')

# Drop rows with missing values
df = df.dropna(subset=['maintext'])

# Preprocess the text data by converting to lowercase and removing punctuation
df['maintext'] = df['maintext'].str.lower()
df['maintext'] = df['maintext'].str.replace('[^\w\s]', '')

# Calculate the sentiment of each token using the VADER library
def calculate_sentiment(text):
    sentiment_scores = []
    for token in text:
        score = analyzer.polarity_scores(token)
        sentiment_scores.append(score['compound'])
    return sum(sentiment_scores) / len(sentiment_scores)

df['sentiment'] = df['maintext'].apply(calculate_sentiment)

# Convert the 'date_publish' column to datetime objects
df['date_publish'] = pd.to_datetime(df['date_publish'], format='%Y-%m-%d %H:%M:%S')

# Filter out rows with invalid or missing strings
mask = df['date_publish'].notnull()
df = df[mask]

# Convert the 'date_publish' column to datetime objects, setting invalid strings to NaN
df['date_publish'] = pd.to_datetime(df['date_publish'], format='%Y-%m-%d %H:%M:%S', errors='coerce')

# Extract the month and year from the 'date_publish' column
df['month'] = df['date_publish'].apply(lambda x: x.strftime('%Y-%m'))

# Aggregate the sentiment scores by time period (e.g., month)
sentiment_by_month = df.groupby('month')['sentiment'].mean()

# Visualize the sentiment over time using the matplotlib library
plt.plot(sentiment_by_month.index, sentiment_by_month.values)
plt.xlabel('Month')
plt.ylabel('Sentiment Score')
plt.title('Sentiment Over Time')
plt.show()
