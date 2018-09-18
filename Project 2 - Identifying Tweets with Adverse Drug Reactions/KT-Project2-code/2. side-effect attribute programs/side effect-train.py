#identify whether a tweet contains the bigram-word:"side effect"

import csv

with open('train.txt', 'r', encoding='ISO-8859-1') as traintxt:
    for row in csv.reader(traintxt):
        if 'side effect' in row[-1]:
            print('1')
        else:
            print('0')
 

