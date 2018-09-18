#generate "sentiment" attribute values for the development data set
#using the "vanderSensiment" package from:
#https://pypi.python.org/pypi/vaderSentiment

import csv
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

#read the development data set line by line
with open('dev.txt', 'r') as dev_tweets:
    for row in csv.reader(dev_tweets):
        sentence = row[-1]
        score = analyzer.polarity_scores(sentence)
        if score['compound'] >= 0:
            print('1')
        else:
            print('0')
 

