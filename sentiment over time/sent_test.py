
import pandas as pd
import glob
import json
import os


#test:
sentence = " you are a very bad guy"



from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer as SIA  
sid_obj1 = SIA()


sentiment = sid_obj1.polarity_scores(sentence)

print(sentiment)


#actual sentiment:

#read dataframe
scraped_web = pd.read_csv('/Users/sorenmeiner/Library/CloudStorage/OneDrive-Aarhusuniversitet/CogComm exam/telegram-analysis-master/csv_data/ukraine_translate_final.csv')

#making a list called "sentences" out of the column with sentences in the dataframe. in this example it is column 9 in the scraped web df
sentences = scraped_web[scraped_web.columns[10]].values.tolist()

#converting the list into sentences
sentences = [str(x) for x in sentences]
print('converting sentences to strings')

# i dont think this is important, but i dont remember so ill keep it.
#scraped_web["maintext"] = scraped_web["maintext"].astype(str)

#importing sentimen analyser
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer as SIA  
sid_obj1 = SIA()

#counter for progress bar
counter = 0

#creating new lists to later make a datafram from
sentiment = []
compound = []


# aplying sentiment analyser on all sentences and the printing and counter part is just a progress bar.
for sentence in sentences:
    counter += 1
    print("percentage completed:",counter/len(sentences)*100, end='\r')
    sentiment.append(sid_obj1.polarity_scores(sentence)) #sentiment on sentence

for i in sentiment:
    compound.append(i.get('compound'))

for i in sentiment:
  i.pop('compound')


#creating dataframe with the column sentence
df = pd.DataFrame(sentences, columns=['sentence'])

#appending the lists sentiment and compound 
df['sentiment'] = sentiment
df['compound'] = compound



# appending additional stuff to the new datafram from the old data frame, 
# so new df['title] is taken from old df here defined as scraped_web from the column called ['title']
df['message'] = scraped_web['message']
df['date_publish'] = scraped_web['date']
df['source_domain'] = scraped_web['peer_id']
#df['url'] = scraped_web['url']


#printing first 10 rows
print(df.head(10))



#exporting csv.
df.to_csv('/Users/sorenmeiner/Library/CloudStorage/OneDrive-Aarhusuniversitet/CogComm exam/sentiment over time/sentiment_data/sent_ukraine_tele.csv', index=False) 