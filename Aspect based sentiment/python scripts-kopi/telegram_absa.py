
#link = https://towardsdatascience.com/aspect-based-sentiment-analysis-using-spacy-textblob-4c8de3e0d2b9

import spacy
nlp = spacy.load("en_core_web_sm")
import pandas as pd
import glob
import json
import os

#loading in the datafile from the raw scraped data.
scraped_telegram = pd.read_csv('/Users/thorkildkappel/Library/CloudStorage/OneDrive-Aarhusuniversitet/CogComm exam/data/csv.csv')

#print(scraped_telegram.head())

sentences = scraped_telegram[scraped_telegram.columns[4]].values.tolist()
#print(sentences)

sentences = [str(x) for x in sentences]

for sentence in sentences:
  doc = nlp(sentence)
  for token in doc:
    #print(token.text, token.dep_, token.head.text, token.head.pos_,
      token.pos_,[child for child in token.children]


for sentence in sentences:
  doc = nlp(sentence)
  descriptive_term = ''
  for token in doc:
    if token.pos_ == 'ADJ':
      descriptive_term = token
  #print(sentence)
  #print(descriptive_term)



for sentence in sentences:
  doc = nlp(sentence)
  descriptive_term = ''
  for token in doc:
    if token.pos_ == 'ADJ':
      prepend = ''
      for child in token.children:
        if child.pos_ != 'ADV':
          continue
        prepend += child.text + ' '
      descriptive_term = prepend + token.text
  #print(sentence)
  #print(descriptive_term)


# tokenization
aspects = []
for sentence in sentences:
  doc = nlp(sentence)
  descriptive_term = ''
  target = ''
  for token in doc:
    if token.dep_ == 'nsubj' and token.pos_ == 'NOUN':
      target = token.text
    if token.pos_ == 'ADJ':
      prepend = ''
      for child in token.children:
        if child.pos_ != 'ADV':
          continue
        prepend += child.text + ' '
      descriptive_term = prepend + token.text
  aspects.append({'aspect': target,
    'description': descriptive_term})
#print(aspects)


#sentiment with textblob:
#from textblob import TextBlob
#for aspect in aspects:
  #aspect['sentiment'] = TextBlob(aspect['description']).sentiment
#print(aspects)

#sentiment intensity analysis with vader
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer as SIA  
sid_obj1 = SIA()

for aspect in aspects:
  aspect['sentiment'] = sid_obj1.polarity_scores(aspect['description']) #making new collumn using sentiment analysis on the column description

#print(aspects)

#we now have a coloumn called sentiment where we have both neg:, neu:, pos:, and compound:
#but we want to make compound a column of itself:
#making new column in aspect called compound 
for aspect in aspects:
  aspect['compound'] = aspect['sentiment'].get('compound')

#deleting compound value from the sentiment column
for aspect in aspects:
  aspect['sentiment'].pop('compound')

#making it a pandas dataframe
df = pd.DataFrame(aspects)

#append date
df['date'] = scraped_telegram['date']

df['Author'] = scraped_telegram['post_author']

# Write the DataFrame to a CSV file (because dropna() doesnt work on the file right now)
df.to_csv('/Users/thorkildkappel/Desktop/1_Semester/Cog com/csv/aspects.csv', index=False)

# reading in the csv 
df = pd.read_csv('/Users/thorkildkappel/Desktop/1_Semester/Cog com/csv/aspects.csv')


#filtering out NA cells from the csv file  (this would be way more effecient if we could do it before we deployed vader)
new_df = df.dropna()


print(new_df.head())
#updating the csv-file
new_df.to_csv('/Users/thorkildkappel/Desktop/1_Semester/Cog com/csv/aspects.csv', index=False)

#mean compound:
from statistics import mean
print("mean compound:" ,mean(df["compound"]))

