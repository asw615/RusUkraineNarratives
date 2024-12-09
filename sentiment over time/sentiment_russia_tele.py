# Import necessary libraries
import pandas as pd
from textblob import TextBlob

# Load the text data into a pandas DataFrame
df = pd.read_csv('/Users/sorenmeiner/Library/CloudStorage/OneDrive-Aarhusuniversitet/CogComm exam/telegram-analysis-master/csv_data/russia_translate_final.csv')

# Drop rows with missing values
df = df.dropna(subset=['english'])

# Preprocess the text data by converting to lowercase and removing punctuation
df['english'] = df['english'].str.lower()
df['english'] = df['english'].str.replace('[^\w\s]','')

# Split the text data into individual tokens using the TextBlob library
df['tokens'] = df['english'].apply(lambda x: TextBlob(x).words)

# Calculate the sentiment of each token using the TextBlob library
df['sentiment'] = df['english'].apply(lambda x: TextBlob(x).sentiment.polarity)

# Import the datetime library
import datetime

# Convert the 'date' column to datetime objects
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%dT%H:%M:%SZ')

# Create a datetime object for 2022/01/01
start_date = datetime.datetime(2022, 1, 1)

# Filter out rows with timestamps before 2022/01/01
mask = df['date'] >= start_date
df = df[mask]

# Filter out rows with invalid or missing strings
mask = df['date'].notnull()
df = df[mask]

# Convert the 'date' column to datetime objects, setting invalid strings to NaN
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%dT%H:%M:%SZ', errors='coerce')

# Extract the month from the 'date' column
df['month'] = df['date'].apply(lambda x: x.strftime('%Y-%m'))

# Aggregate the sentiment scores by time period (e.g., month)
df['month'] = df['date'].apply(lambda x: x.strftime('%Y-%m'))
sentiment_by_month = df.groupby('month')['sentiment'].mean()

# Visualize the sentiment over time using the matplotlib library
import matplotlib.pyplot as plt
plt.plot(sentiment_by_month.index, sentiment_by_month.values)
plt.xlabel('Month')
plt.ylabel('Sentiment Score')
plt.title('Sentiment Over Time')
plt.show()
