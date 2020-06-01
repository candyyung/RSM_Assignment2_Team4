import pandas as pd
from textblob import TextBlob
import os
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import re
from langdetect import detect

data = pd.read_csv('../../gen/data-preparation/temp/parsed-data.csv', sep = '\t')
data.head()


for i, j in data.iterrows():
    print(i)
    try:
        #blob = TextBlob(j['text'])
        data.loc[i, 'text'] = re.sub('http://\S+|https://\S+', '', data.loc[i, 'text']) #remove url
        sentence = data.loc[i, 'text']
        analyser = SentimentIntensityAnalyzer()
        
        data.loc[i, 'language'] = detect(sentence) #detect main language used in the text
        
        # polarity score and subjectivity score
        blob = TextBlob(sentence)
        polarity_scores = analyser.polarity_scores(blob)
        data.loc[i, 'polarity'] = blob.sentiment.polarity
        data.loc[i, 'subjectivity'] = blob.sentiment.subjectivity
        

        data.loc[i, 'neg'] = analyser.polarity_scores(sentence)['neg'] #negative score
        data.loc[i, 'neu'] = analyser.polarity_scores(sentence)['neu'] #neutral score
        data.loc[i, 'pos'] = analyser.polarity_scores(sentence)['pos'] #positive score
        data.loc[i, 'compound'] = analyser.polarity_scores(sentence)['compound'] #overall valence score of the text
       
        #count the total number of words 
        data.loc[i, 'nwords'] = len(blob.words)
        
        #count the number of specific words
        wordcount = 0
        lower = sentence.lower()
        target_words = ['travisscott', 'travis scott', 'trvisXX']
        for target in target_words:
            wordcount+=lower.count(target)
        data.loc[i, 'travisscott'] = wordcount 

        wordcount2 = 0
        target_words2 = ['fortnite']
        for target in target_words2:
            wordcount2+=lower.count(target)
        data.loc[i, 'fortnite'] = wordcount2 
        
        wordcount3 = 0
        target_words3 = ['astronomical']
        for target in target_words3:
            wordcount3+=lower.count(target)
        data.loc[i, 'astronomical'] = wordcount3 

    except:
        data.loc[i, 'language'] = ''
        data.loc[i, 'neg'] = ''
        data.loc[i, 'neu'] = ''
        data.loc[i, 'pos'] = ''
        data.loc[i, 'compound'] = ''
        data.loc[i, 'travisscott'] = ''
        data.loc[i, 'fortnite'] = ''
        data.loc[i, 'astronomical'] = ''
        #data.loc[i, 'polarity'] = ''
        #data.loc[i, 'subjectivity'] = ''

data.head()

os.makedirs('../../gen/data-preparation/output/', exist_ok=True)

data.to_csv('../../gen/data-preparation/output/dataset.csv', index = False)

print('done.')



        #textblob = TextBlob(sentence)/textblob.detect_language()
        #print(analyser.polarity_scores(sentence))
      