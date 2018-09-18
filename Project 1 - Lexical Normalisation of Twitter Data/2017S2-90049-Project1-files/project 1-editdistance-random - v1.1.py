#Find the best match vs canonical for tokens using Global Edit Distance
#Parameters are Levenshtein Distance
#using the “editdistance” package from:
#https://pypi.python.org/pypi/editdistance


import csv
import editdistance

print('% -15s %-15s %-15s % -15s'%('Token','Best Match','Canonical Form','Best Val')) #print the header

candidate_tk_num = 0
right_match_num = 0

# read each row of labelled tokens line by line
with open('labelled-tokens.txt', 'r',encoding='ISO-8859-1') as labelled_tokens:
    for row in csv.reader(labelled_tokens, delimiter = '\t'):
        if row[-2] == 'OOV': #candidte for normalisation
            #row[-3] is Token;
            #row[-2] is Code;
            #row[-3] is Canonical Form
            candidate_tk_num += 1
            dict_file = open('dict.txt', 'r')  #open dictionary
            best_val = 999999999999999
            best_match = ''
            for line in dict_file:
                val = editdistance.eval(row[-3], line.strip())
                if val < best_val:
                    best_val = val
                    best_match = line.strip()
           
            if best_match != row[-1]:
                print('% -15s %-15s %-15s % -15s'%(row[-3],best_match, row[-1],best_val))
            elif best_match == row[-1]:
                right_match_num += 1
                
    #print(right_match_num)
    #print(candidate_tk_num)
    accurary = right_match_num/candidate_tk_num
    print("%.2f" % accurary)
 

           
           

