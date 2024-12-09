import pandas as pd

# Load the data into a DataFrame
df = pd.read_csv('/Users/sorenmeiner/Library/CloudStorage/OneDrive-Aarhusuniversitet/CogComm exam/webscraper/csv_data/df_russia.csv')

# Select rows where the 'Name' column contains the word 'John'
filtered_df = df[~df['filename'].str.contains('sputniknews.com')]



# save dataframe to csv
filtered_df.to_csv('/Users/sorenmeiner/Library/CloudStorage/OneDrive-Aarhusuniversitet/CogComm exam/webscraper/csv_data/df_russia_!sputniknews.csv')