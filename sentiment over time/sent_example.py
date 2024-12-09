import pandas as pd
import glob
import json
import os


#test:
sentence = "The Russians are having a difficult time"



from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer as SIA  
sid_obj1 = SIA()


sentiment = sid_obj1.polarity_scores(sentence)

print(sentiment)
