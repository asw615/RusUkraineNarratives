from newsplease import NewsPlease
from newsplease.config import JsonConfig
import json
import os
import pandas as pd
import glob


article = NewsPlease.from_url('https://en.news-front.info/2022/12/09/russian-armys-reinforcement-marks-turning-point-in-ukraine-conflict-newsweek/')

with open(article.filename, 'w') as outfile:
    json.dump(article.get_serializable_dict(), outfile, indent=4, sort_keys=True)

# making sure there is a logfile directory
if not os.path.exists("csv_data"):
    os.makedirs("csv_data")

# Making an empty table
df_list = []

#loading in data from the database and concat them into a single dataframe
for curr_file in glob.glob("*.json"):
    json_data = json.load(open(curr_file))
    df = pd.DataFrame(json_data)
    df_list.append(df)

pdf = pd.concat(df_list)

pdf.to_csv("csv_data/newsfront.csv",index=False)