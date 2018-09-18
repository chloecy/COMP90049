#Combine GED and N-Gram to increase system precision
#using the “editdistance” package from:
#https://pypi.python.org/pypi/editdistance
#using the “Ngram” package from:
#https://pypi.python.org/pypi/ngram

import csv
import ngram
import editdistance

print('% -15s %-15s %-15s'%('Token','Best Match','Canonical Form')) #print the header

OOV_num = 0
right_match_count = 0
multiple_attempt_count = 0

# read each row of labelled tokens line by line
with open('labelled-tokens.txt', 'r',encoding='ISO-8859-1') as labelled_tokens:
    for row in csv.reader(labelled_tokens, delimiter = '\t'):
        if row[-2] == 'OOV': #candidte for normalisation
            #row[-3] is Token;
            #row[-2] is Code;
            #row[-3] is Canonical Form
            OOV_num += 1

            dict_file = open('dict.txt', 'r')  #open dictionary
            best_val1 = 999999999999999
            best_match = ''

            for line in dict_file:  #find the minimum edit distance
                val1 = editdistance.eval(row[-3], line.strip())
                if val1 < best_val1:
                    best_val1 = val1
            
            best_matches_list = []
            dict_file = open('dict.txt', 'r')  #open dictionary
            for line in dict_file:  #find the best match(es)
                if editdistance.eval(row[-3], line.strip()) == best_val1:
                   best_matches_list.append(line.strip())

            if row[-1] in best_matches_list:
                right_match_count += 1
                multiple_attempt_count += 1
                best_match = row[-1]
                print('% -15s %-15s %-15s'%(row[-3], best_match,row[-1]))
            else:
                dict_file = open('dict.txt', 'r')  #open dictionary
                best_val2 = 0
                best_match2 = ''
                for x in best_matches_list:
                    val2 = ngram.NGram.compare(x, line.strip(), N=2)
                    if val2 > best_val2:
                        best_val2 = val2
                        
                for x in best_matches_list:
                    if ngram.NGram.compare(x, line.strip(), N=2) == best_val2:
                        multiple_attempt_count += 1
                        best_match2 = x
                        print('% -15s %-15s %-15s'%(row[-3],best_match2, row[-1]))
                
                    

precision = right_match_count / multiple_attempt_count
recall = right_match_count / OOV_num
print('precision', '%.4f' % precision)
print('recall', '%.4f' % recall)
print(right_match_count)
print(multiple_attempt_count)
print(OOV_num)
