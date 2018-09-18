#generate "sentiment" attribute values for the test data set
#using the "vanderSensiment" package from:
#https://pypi.python.org/pypi/vaderSentiment

import csv
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

#read the test data set line by line
with open('test.txt', 'r') as test_tweets:
    for row in csv.reader(test_tweets):
        sentence = row[-1]
        score = analyzer.polarity_scores(sentence)
        if score['compound'] >= 0:
            print('1')
        else:
            print('0')      
      
