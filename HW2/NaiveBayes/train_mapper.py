#!/usr/bin/env python
"""
Mapper reads in text documents and emits word counts by class.
INPUT:                                                    
    DocID \t true_class \t subject \t body                
OUTPUT:                                                   
    partitionKey \t word \t class0_partialCount,class1_partialCount       
    

Instructions:
    You know what this script should do, go for it!
    (As a favor to the graders, please comment your code clearly!)
    
    A few reminders:
    1) To make sure your results match ours please be sure
       to use the same tokenizing that we have provided in
       all the other jobs:
         words = re.findall(r'[a-z]+', text-to-tokenize.lower())
         
    2) Don't forget to handle the various "totals" that you need
       for your conditional probabilities and class priors.
       
Partitioning:
    In order to send the totals to each reducer, we need to implement
    a custom partitioning strategy.
    
    We will generate a list of keys based on the number of reduce tasks 
    that we read in from the environment configuration of our job.
    
    We'll prepend the partition key by hashing the word and selecting the
    appropriate key from our list. This will end up partitioning our data
    as if we'd used the word as the partition key - that's how it worked
    for the single reducer implementation. This is not necessarily "good",
    as our data could be very skewed. However, in practice, for this
    exercise it works well. The next step would be to generate a file of
    partition split points based on the distribution as we've seen in 
    previous exercises.
    
    Now that we have a list of partition keys, we can send the totals to 
    each reducer by prepending each of the keys to each total.
       
"""

import re                                                   
import sys                                                  
import numpy as np      

from operator import itemgetter
import os

#################### YOUR CODE HERE ###################
def getPartitionKey(word):
    """ 
    Helper function to assign partition key ('A' or 'B').
    Args:  word (str) 
    """
    if word[0] < 'm':
        return  'A'
    else:
        return 'B'

#Read in data
for line in sys.stdin:
    line = line.strip()
    
    #tokenize
    docID, true_class, subject, body = line.lower().split('\t')
    words = re.findall(r'[a-z]+', subject + ' ' + body)
    
    #Setting ham/spam toggle
    ham,spam = 0,0
    if true_class == '0':
        ham = '1'
    else:
        spam = '1'
    
    #Output
    print(f'A\t*docIDTotal\t{ham},{spam}') #docIDTotal to partition A
    print(f'B\t*docIDTotal\t{ham},{spam}') #docIDTotal to partition B
    for word in words:
        pKey = getPartitionKey(word[0]) #1st letter of word defines category
        print(f'{pKey}\t{word}\t{ham},{spam}')
        print(f'A\t*WrdTotal\t{ham},{spam}') #WrdTotal to partition A
        print(f'B\t*WrdTotal\t{ham},{spam}') #WrdTotal to partition B


#################### (END) YOUR CODE ###################