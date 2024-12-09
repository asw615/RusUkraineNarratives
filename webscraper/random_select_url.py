import pandas as pd
import random

# List of file paths
file_paths = [
    '/Users/sorenmeiner/Library/CloudStorage/OneDrive-Aarhusuniversitet/CogComm exam/webscraper/URL/tsn.csv', 
    '/Users/sorenmeiner/Library/CloudStorage/OneDrive-Aarhusuniversitet/CogComm exam/webscraper/URL/kyiv_ind.csv',
    '/Users/sorenmeiner/Library/CloudStorage/OneDrive-Aarhusuniversitet/CogComm exam/webscraper/URL/kyiv_post.csv',
    ]

# Initialize empty list to store selected URLs
selected_urls = []

# Iterate over each file path
for file_path in file_paths:
    # Read the CSV file and store the resulting DataFrame in a variable
    df = pd.read_csv(file_path)
    
    # Select the minimum of the number of rows in the DataFrame and the desired number of URLs
    num_urls = min(df.shape[0], 3000)

    # Use the random.sample() function to randomly select the desired number of rows from the DataFrame
    sample = random.sample(df.index.tolist(), k=num_urls)
    
    # Extract the URLs from the selected rows
    urls = df.loc[sample, 'url']
    
    # Append the selected URLs to the list
    selected_urls.extend(urls)

# Create a new DataFrame with a single column containing the selected URLs
selected_urls_df = pd.DataFrame({'url': selected_urls})

# Write the new DataFrame to a CSV file
selected_urls_df.to_csv('/Users/sorenmeiner/Library/CloudStorage/OneDrive-Aarhusuniversitet/CogComm exam/webscraper/URL_TO_SCRAPE/ukranian/ukranian_urls.csv', index=False)
