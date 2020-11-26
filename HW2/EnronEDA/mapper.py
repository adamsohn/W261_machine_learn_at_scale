#!/usr/bin/env python
"""
Mapper tokenizes and emits words with their class.
INPUT:
    ID \t SPAM \t SUBJECT \t CONTENT \n
OUTPUT:
    word \t class \t count 
"""
import re
import sys

# read from standard input
for line in sys.stdin:
    # parse input
    docID, _class, subject, body = line.split('\t')
    # tokenize
    words = re.findall(r'[a-z]+', subject + ' ' + body)
    
############ YOUR CODE HERE #########
    word_list_of_list = ([[word, words.count(word)] for word in set(words)])
    for i in range(len(word_list_of_list)):
        print(f'{word_list_of_list[i][0]}\t{_class}\t{word_list_of_list[i][1]}')

############ (END) YOUR CODE #########