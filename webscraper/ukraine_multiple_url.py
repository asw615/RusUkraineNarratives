from newsplease import NewsPlease
from newsplease.config import JsonConfig
import json
import os
import pandas as pd
import glob

# Making sure a json data folder exists
if not os.path.exists("json_data"):
        os.makedirs("json_data")

# Read all CSV files in the current directory
csv_files = glob.glob("/Users/sorenmeiner/Library/CloudStorage/OneDrive-Aarhusuniversitet/CogComm exam/webscraper/URL_TO_SCRAPE/russian/russian_urls.csv")

# Create an empty list to store the DataFrames
df_list = []

# Loop through the CSV files and read them into a DataFrame
for filename in csv_files:
    df = pd.read_csv(filename)
    df_list.append(df)

# Concatenate the DataFrames into a single DataFrame
df = pd.concat(df_list)

df = df.dropna(subset=['url'])

# Extract the URLs from the "URL" column of the DataFrame
article_list = df["url"].tolist()


for i in article_list:
    article = NewsPlease.from_url(i)
    # Using string formatting
    if article.authors == []:
        article.authors = [article.url]
    file_path = '/Users/sorenmeiner/Library/CloudStorage/OneDrive-Aarhusuniversitet/CogComm exam/webscraper/json_data/russian_articles01/other/{}'.format(article.filename)
    with open(file_path, 'w') as outfile:
        json.dump(article.get_serializable_dict(), outfile, indent=4, sort_keys=True)


# making sure there is a logfile directory
if not os.path.exists("csv_data"):
    os.makedirs("csv_data")
    

# Making an empty table
df_list = []
#loading in data from the database and concat them into a single dataframe
for curr_file in glob.glob("/Users/sorenmeiner/Library/CloudStorage/OneDrive-Aarhusuniversitet/CogComm exam/webscraper/json_data/russian_articles01/other/*.json"):
    json_data = json.load(open(curr_file))
    df = pd.DataFrame(json_data)
    df_list.append(df)

pdf = pd.concat(df_list)

# Removing duplicates
pdf_no_duplicates = pdf.drop_duplicates(subset=['url'])

pdf_no_duplicates.to_csv("csv_data/russia_wo_tass.csv",index=False)