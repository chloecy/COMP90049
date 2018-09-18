#Calculate the proportion of "OOV" tokens with a canonical form the same as itself
#as well as the proportion of difference

import csv

OOV_tk_num = 0
right_match_num = 0
wrong_match_num = 0

# read each row of labelled tokens line by line
with open('labelled-tokens.txt', 'r',encoding='ISO-8859-1') as labelled_tokens:
    for row in csv.reader(labelled_tokens, delimiter = '\t'):
        if row[-2] == 'OOV' : 
            #row[-3] is Token;
            #row[-2] is Code;
            #row[-3] is Canonical Form
            OOV_tk_num += 1
            
            if row[-3] == row[-1]:
                right_match_num += 1
            else:
                wrong_match_num += 1
                

accurary = right_match_num / OOV_tk_num
error_rate = wrong_match_num / OOV_tk_num
print('right match num:', right_match_num)
print('wrong_match num:', wrong_match_num)
print('OOV num:', OOV_tk_num)
print('accurary', "%.4f" % accurary)
print('error rate', "%.4f" % error_rate)
 

           
           

