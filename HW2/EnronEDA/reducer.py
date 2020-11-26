#!/usr/bin/env python
"""
Reducer takes words with their class and partial counts and computes totals.
INPUT:
    word \t class \t partialCount 
OUTPUT:
    word \t class \t totalCount  
"""
import re
import sys

# initialize trackers
current_word = None 
spam_count, ham_count = 0,0

#for line in [('one',1,1),('one',0,1),('one',0,1),('two',0,1)]


# read from standard input
for line in sys.stdin:
    # parse input
    word, is_spam, count = line.split('\t')
    
############ YOUR CODE HERE #########
    if word != current_word: #new word
        if current_word:
            print(f'{current_word}\t{1}\t{spam_count}') #prior word
            print(f'{current_word}\t{0}\t{ham_count}')    #prior word    
            if is_spam == str(1):
                spam_count = int(count)
            else:
                ham_count = int(count)
        current_word = word
        continue
    else: #not 1st instance of word.
        if is_spam == str(1):
            spam_count += int(count)
        else:
            ham_count += int(count)
        current_word = word
print(f'{current_word}\t{1}\t{spam_count}') #last word
print(f'{current_word}\t{0}\t{ham_count}')    #last word               

############ (END) YOUR CODE #########