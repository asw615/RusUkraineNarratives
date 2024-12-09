import re
import pandas as pd

def extract_date(text):
  date_pattern = r'([A-Za-z]+\s+\d+)'
  date = re.search(date_pattern, text)
  if date:
    return date.group(1)
  else:
    return ''

# Load the data into a Pandas DataFrame
df = pd.read_csv('/Users/sorenmeiner/Library/CloudStorage/OneDrive-Aarhusuniversitet/CogComm exam/webscraper/csv_data/tass_wo_dates.csv')

# Create a new column for the dates
df['dates'] = ''

# Iterate through each row of the maintext column
for index, row in df['maintext'].iteritems():
  # Extract the date from the maintext
  date = extract_date(row)
  # Update the dates column with the extracted date
  df.at[index, 'dates'] = date

# Save the updated DataFrame to a new CSV file
df.to_csv('/Users/sorenmeiner/Library/CloudStorage/OneDrive-Aarhusuniversitet/CogComm exam/webscraper/csv_data/tass_w_dates_newcolumn.csv', index=False)