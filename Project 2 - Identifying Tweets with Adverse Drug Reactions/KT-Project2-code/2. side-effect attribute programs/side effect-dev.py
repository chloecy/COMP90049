#identify whether a tweet contains the bigram-word:"side effect"

import csv

with open('dev.txt', 'r', encoding='ISO-8859-1') as devtxt:
    for row in csv.reader(devtxt):
        if 'side effect' in row[-1]:
            print('1')
        else:
            print('0')
 

