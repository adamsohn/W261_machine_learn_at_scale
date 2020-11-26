#!/usr/bin/env python
"""
Reducer aggregates word counts by class and emits frequencies.

INPUT:
    partitionKey \t word \t class0_partialCount,class1_partialCount
OUTPUT:
    word \t class_0totalCount,class_1totalCount,P(c|word),P(~c|word) 
    
Instructions:
    Again, you are free to design a solution however you see 
    fit as long as your final model meets our required format
    for the inference job we designed in Question 8. Please
    comment your code clearly and concisely.
    
    A few reminders: 
    1) Don't forget to emit Class Priors (with the right key).
    2) In python2: 3/4 = 0 and 3/float(4) = 0.75
"""
##################### YOUR CODE HERE ####################
import re                                                   
import sys                                                  
import numpy as np      

from operator import itemgetter
import os

word = None
curr_word = '_begin'
N_spam1_wc = 0
N_ham0_wc = 0
N_spam1_record = 0
N_ham0_record = 0
spam1_wc = 0 
ham0_wc = 0


for line in sys.stdin: 
    partitionKey, word, partialCount = line.strip().split('\t')
    class0_partialCount,class1_partialCount = partialCount.split(',')

    #Collecting Totals
    if word == '*docIDTotal':
        if class0_partialCount == '0':
            N_ham0_record += 1
        else:
            N_spam1_record += 1            
        continue

    elif word == '*WrdTotal':
        if class0_partialCount == '0':
            N_ham0_wc += 1
        else:
            N_spam1_wc += 1                    
        continue  
    
    #Noting the moment we are past the totals so we can start processing 'actual' records. Emitting ClassPrior
    if curr_word == '_begin':
        total_rcd =  N_ham0_record + N_spam1_record    
        print(f'ClassPrior\t{N_ham0_record},{N_spam1_record}, {float(N_ham0_record/(total_rcd))},{float(N_spam1_record/(total_rcd))}')
        
        #processing first occurence of real word
        curr_word = word
        if class0_partialCount == '0':
            ham0_wc += 1
        else:
            spam1_wc += 1
        continue
        
    #At the moment a word stops repeating, emit the result for the prior word (known as curr_word until curr_word is reset)
    elif word != curr_word:
        try: #catching div-by-0
            P_ham_wrd = float(ham0_wc/N_ham0_wc)
            P_spam_wrd = float(spam1_wc/N_spam1_wc)
        except:
            P_ham_wrd = 0
            P_spam_wrd = 0           
        print(f'{curr_word}\t{ham0_wc},{spam1_wc},{P_ham_wrd},{P_spam_wrd}')

        curr_word = word
        if class0_partialCount == '0':
            ham0_wc += 1
        else:
            spam1_wc += 1           
        continue

    #Repeat occurence
    elif word == 'curr_word':
        if class0_partialCount == '0':
            ham0_wc += 1
        else:
            spam1_wc += 1               

#Printing final word
try: #catching div-by-0
    P_ham_wrd = float(ham0_wc/N_ham0_wc)
    P_spam_wrd = float(spam1_wc/N_spam1_wc)
except:
    P_ham_wrd = 0
    P_spam_wrd = 0    
print(f'{word}\t{ham0_wc},{spam1_wc},{P_ham_wrd},{P_spam_wrd}')
##################### (END) CODE HERE ####################