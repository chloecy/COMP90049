#generate "sentiment" attribute values for the training data set
#using the "vanderSensiment" package from:
#https://pypi.python.org/pypi/vaderSentiment

import csv
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

#read the training data set line by line
with open('train.txt', 'r') as train_tweets:
    for row in csv.reader(train_tweets):
        sentence = row[-1]
        score = analyzer.polarity_scores(sentence)
        if score['compound'] >= 0:
            print('1')
        else:
            print('0')
      
