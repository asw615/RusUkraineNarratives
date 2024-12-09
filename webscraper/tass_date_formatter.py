import re
import pandas as pd
from datetime import datetime

def extract_date(text):
  date_pattern = r'([A-Za-z]+\s+\d+)'
  date = re.search(date_pattern, text)
  if date:
    return date.group(1)
  else:
    return ''

# Load the data into a Pandas DataFrame
df = pd.read_csv('/Users/sorenmeiner/Library/CloudStorage/OneDrive-Aarhusuniversitet/CogComm exam/webscraper/csv_data/tass_w_dates_newcolumn.csv')

# Create a new column for the dates
df['date_publish'] = ''

# Iterate through each row of the maintext column
for index, row in df['dates'].iteritems():
  # Extract the date from the maintext
  date = extract_date(row)
  if date:
    # Format the date as '%Y-%m-%d %H:%M:%S' with the year set to 2022
    formatted_date = datetime.strptime(date + ' 2022', '%B %d %Y').strftime('%Y-%m-%d %H:%M:%S')
    df.at[index, 'date_publish'] = formatted_date
    
# Save the updated DataFrame to a new CSV file
df.to_csv('/Users/sorenmeiner/Library/CloudStorage/OneDrive-Aarhusuniversitet/CogComm exam/webscraper/csv_data/tass_dates_formatted.csv', index=False)