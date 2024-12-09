
import pandas as pd
import statistics

df = pd.read_csv('/Users/thorkildkappel/Desktop/1_Semester/Cog com/csv/aspects.csv')


df['aspect'] = df['aspect'].str.lower() #makes everything to lower because it helps with sorting
averages = df.groupby('aspect')['compound'].mean() # grouping words an getting the mean compopund
sd = df.groupby('aspect')['compound'].std()
new_df = pd.DataFrame(averages) #converting to a dataframe
new_df['n'] = df.aspect.value_counts() #adding the amount of same words
new_df['sd'] = sd

# to get a full dataframe with aspect included
new_df = new_df.reset_index()

#sorting it by number of word
new_df = new_df.sort_values(by=['n'], ascending=False)

#print to see if it looks okay
print(new_df.head(10))

#making a csv-file
new_df.to_csv('/Users/thorkildkappel/Desktop/1_Semester/Cog com/csv/summary.csv', index=False)