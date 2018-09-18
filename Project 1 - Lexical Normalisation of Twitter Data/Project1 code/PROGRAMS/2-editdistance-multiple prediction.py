#Find the best match for tokens using Global Edit Distance
#Parameters are Levenshtein Distance
#using the “editdistance” package from:
#https://pypi.python.org/pypi/editdistance


import csv
import editdistance

right_match_count = 0
multiple_attempt_count = 0
OOV_num = 0

print('% -15s %-15s %-15s % -15s'%('Token','Best Match','Canonical Form','Best Val')) #print the header

# read each row of labelled tokens line by line
with open('labelled-tokens.txt', 'r',encoding='ISO-8859-1') as labelled_tokens:
    for row in csv.reader(labelled_tokens, delimiter = '\t'):
        if row[-2] == 'OOV': #candidte for normalisation
            OOV_num += 1
            #row[-3] is Token;
            #row[-2] is Code;
            #row[-3] is Canonical Form
 
            dict_file = open('dict.txt', 'r')  #open dictionary
            best_val = 999999999999999
            best_match = ''
 
            
            for line in dict_file:  #find the minimum edit distance
                val = editdistance.eval(row[-3], line.strip())
                if val < best_val:
                    best_val = val
                    

            dict_file = open('dict.txt', 'r')  #open dictionary
            for line in dict_file:  #find the best match(es)
                if editdistance.eval(row[-3], line.strip()) == best_val:
                    best_match = line.strip()
                    multiple_attempt_count += 1
                    if best_match == row[-1]:
                        right_match_count += 1
                        print('% -15s %-15s %-15s % -15s'%(row[-3],best_match, row[-1],best_val))
                    else:
                        multiple_attempt_count += 1
                        print('% -15s %-15s %-15s % -15s'%(row[-3],best_match, row[-1],best_val))

precision = right_match_count / multiple_attempt_count
recall = right_match_count / OOV_num
print('precision:', '%.4f'% precision)
print('recall:', '%.4f'% recall)
    
 

           
           

