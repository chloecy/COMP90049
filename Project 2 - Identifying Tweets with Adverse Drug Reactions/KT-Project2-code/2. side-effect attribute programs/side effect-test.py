#identify whether a tweet contains the bigram-word:"side effect"

import csv

with open('test.txt', 'r', encoding='ISO-8859-1') as testtxt:
    for row in csv.reader(testtxt):
        if 'side effect' in row[-1]:
            print('1')
        else:
            print('0')
 

