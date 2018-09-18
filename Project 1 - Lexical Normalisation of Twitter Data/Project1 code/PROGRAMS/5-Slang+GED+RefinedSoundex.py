#Find the best match for tokens using a slang dictonary, GED and Refined Soundex Method.
#Parameters are Levenshtein Distance
#using the “editdistance” package from:
#https://pypi.python.org/pypi/editdistance
#using the “pyphonetics” package from:
#https://pypi.python.org/pypi/pyphonetics/0.4.1
#using a slang_dict from:
#http://www.hlt.utdallas.edu/~yangl/data/Text_Norm_Data_Release_Fei_Liu/

import csv
import editdistance
import re
from pyphonetics import RefinedSoundex

rs = RefinedSoundex()
p = re.compile('^[a-zA-Z]+$')  #to identify whether the "OOV" token contains digits

#print(rs.distance('assign', 'assist', metric='levenshtein'))
#print(rs.distance('pix','pictures',metric='levenshtein'))

print('% -15s %-15s %-15s'%('Token','Best Match','Canonical Form'))

slang_dict = {} #transform slang_dict.txt to a dictionary
with open('Slang_dict.txt', 'r', encoding='ISO-8859-1') as slang:
    for line in csv.reader(slang, delimiter = '\t'):
        slang_dict[line[-2]] = line[-1]


right_match_count = 0  #count the right matches
multiple_attempt_count = 0  #count all the attempts
OOV_num = 0  #count all the labelled tokens


# read each row of labelled tokens line by line
with open('labelled-tokens.txt', 'r', encoding='ISO-8859-1') as labelled_tokens:
    for row in csv.reader(labelled_tokens, delimiter = '\t'):
        if row[-2] == 'OOV' and p.match(row[-3]) != None: #candidte for normalisation
            OOV_num += 1
            #row[-3] is Token;
            #row[-2] is Code;
            #row[-3] is Canonical Form

            best_match = ''
              
            if row[-3] in slang_dict.keys():
                best_match = slang_dict[row[-3]]
                right_match_count += 1
                multiple_attempt_count += 1
                print('% -15s %-15s %-15s'%(row[-3],best_match,row[-1]))
                        
            else:
                dict_file = open('dict.txt', 'r')  #open dictionary
                best_val = 999999999999999
                best_val2 = 999999999999999
                for line1 in dict_file:  #find the minimum edit distance
                    val = editdistance.eval(row[-3], line1.strip())
                    if val < best_val:
                        best_val = val

                dict_file = open('dict.txt', 'r')  #open dictionary
                best_matches = []
                for line2 in dict_file:  #find the best match(es)
                    if editdistance.eval(row[-3], line2.strip()) == best_val:
                        best_match = line2.strip()
                        best_matches.append(best_match)
            

                for x in best_matches:
                    val2 = rs.distance(row[-3], x)
                    if val2 < best_val2:
                        best_val2 = val2
            
                if row[-1] in best_matches:
                    best_match = row[-1]
                    multiple_attempt_count += 1
                    right_match_count += 1
                    print('% -15s %-15s %-15s'%(row[-3],best_match,row[-1]))
                else:
                    for y in best_matches:
                        if rs.distance(row[-3],y) == best_val2:
                            best_match = y
                            multiple_attempt_count += 1
                            print('% -15s %-15s %-15s'%(row[-3],best_match,row[-1]))
                            break

                        
        elif row[-2] == 'OOV' and p.match(row[-3]) == None:#if "OOV" contains digits
            OOV_num += 1
            best_match = row[-3]
            if best_match == row[-1]:
                multiple_attempt_count += 1
                right_match_count += 1
                print('% -15s %-15s %-15s'%(row[-3],best_match,row[-1]))
            else:
                multiple_attempt_count += 1
                print('% -15s %-15s %-15s'%(row[-3],best_match,row[-1]))
                                        
                                                                    
precision = right_match_count / multiple_attempt_count
recall = right_match_count / OOV_num
print('precision:', '%.4f'% precision)
print('recall:', '%.4f'% recall)
print(OOV_num)
print(right_match_count)
print(multiple_attempt_count)
