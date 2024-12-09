# Import the necessary packages
from concurrent.futures import ThreadPoolExecutor
import time
from googletrans import Translator
import pandas as pd
from tqdm import tqdm

# Set the maximum number of threads to use
MAX_THREADS = 8

# Initialize the translator and the ThreadPoolExecutor
translator = Translator()
executor = ThreadPoolExecutor(max_workers=MAX_THREADS)

# Read the DataFrame from the CSV file
df = pd.read_csv('/Users/sorenmeiner/Library/CloudStorage/OneDrive-Aarhusuniversitet/CogComm exam/telegram-analysis-master/csv_data/df_ready_translate.csv')

# Drop rows with empty or null values in the 'message' column
df = df.dropna(subset=['message'])

# Create a new column called 'english'
df['english'] = ""

# Define a function that translates a message using the Translator
def translate_message(message):
    # Translate the message
    translation = translator.translate(message, dest='en')


# Set the chunk size
CHUNK_SIZE = 100

# Use the 'apply' method to apply the translate_message function to each row of the 'message' column
# in chunks of size CHUNK_SIZE
for chunk in df['message'].apply(translate_message, chunksize=CHUNK_SIZE):
    # Add the translated text to the 'english' column
    df['english'] = chunk
    if chunk % 1000 == 0:
        # Save the DataFrame to a CSV file
        df.to_csv('/Users/sorenmeiner/Library/CloudStorage/OneDrive-Aarhusuniversitet/CogComm exam/telegram-analysis-master/csv_data/df_ukraine_translate.csv')


# Save the DataFrame to a CSV file
df.to_csv('/Users/sorenmeiner/Library/CloudStorage/OneDrive-Aarhusuniversitet/CogComm exam/telegram-analysis-master/csv_data/df_ukraine_translate.csv')