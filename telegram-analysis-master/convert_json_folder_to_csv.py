import glob
import json
import pandas as pd
import os

# making sure there is a logfile directory
if not os.path.exists("csv_data"):
    os.makedirs("csv_data")

# Making an empty table
df_list = []

#loading in data from the database and concat them into a single dataframe
for curr_file in glob.glob("/Users/sorenmeiner/Library/CloudStorage/OneDrive-Aarhusuniversitet/CogComm exam/webscraper/json_data/russian_articles/*.json"):
    json_data = json.load(open(curr_file))
    df = pd.DataFrame(json_data)
    df_list.append(df)

pdf = pd.concat(df_list)

pdf.to_csv("/Users/sorenmeiner/Library/CloudStorage/OneDrive-Aarhusuniversitet/CogComm exam/webscraper/csv_data/df_russia.csv",index=False)
