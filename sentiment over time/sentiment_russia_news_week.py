# Import necessary libraries
import pandas as pd
from textblob import TextBlob

# Load the text data into a pandas DataFrame
df = pd.read_csv('/Users/sorenmeiner/Library/CloudStorage/OneDrive-Aarhusuniversitet/CogComm exam/webscraper/csv_data/df_russia.csv')

# Drop rows with missing values
df = df.dropna(subset=['maintext'])

# Preprocess the text data by converting to lowercase and removing punctuation
df['maintext'] = df['maintext'].str.lower()
df['maintext'] = df['maintext'].str.replace('[^\w\s]','')

# Split the text data into individual tokens using the TextBlob library
df['tokens'] = df['maintext'].apply(lambda x: TextBlob(x).words)

# Calculate the sentiment of each token using the TextBlob library
df['sentiment'] = df['maintext'].apply(lambda x: TextBlob(x).sentiment.polarity)

# Convert the 'date_publish' column to datetime objects
df['date_publish'] = pd.to_datetime(df['date_publish'], format='%Y-%m-%d %H:%M:%S')

# Filter out rows with invalid or missing strings
mask = df['date_publish'].notnull()
df = df[mask]

# Convert the 'date_publish' column to datetime objects, setting invalid strings to NaN
df['date_publish'] = pd.to_datetime(df['date_publish'], format='%Y-%m-%d %H:%M:%S', errors='coerce')

# Extract the week from the 'date_publish' column
df['week'] = df['date_publish'].apply(lambda x: x.strftime('%Y-%U'))

# Aggregate the sentiment scores by time period (e.g., week)
df['week'] = df['date_publish'].apply(lambda x: x.strftime('%Y-%U'))
sentiment_by_week = df.groupby('week')['sentiment'].mean()

# Visualize the sentiment over time using the matplotlib library
import matplotlib.pyplot as plt
plt.plot(sentiment_by_week.index, sentiment_by_week.values)
plt.xlabel('Week')
plt.ylabel('Sentiment Score')
plt.title('Sentiment Over Time')
plt.show()