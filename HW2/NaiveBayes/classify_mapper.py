#!/usr/bin/env python
"""
Mapper for Naive Bayes Inference.
INPUT:
    ID \t true_class \t subject \t body \n
OUTPUT:
    ID \t true_class \t logP(ham|doc) \t logP(spam|doc) \t predicted_class
SUPPLEMENTAL FILE: 
    This script requires a trained Naive Bayes model stored 
    as NBmodel.txt in the current directory. The model should 
    be a tab separated file whose records look like:
        WORD \t ham_count,spam_count,P(word|ham),P(word|spam)
        
Instructions:
    We have loaded the supplemental file and taken the log of 
    each conditional probability in the model. We also provide
    the code to tokenize the input lines for you. Keep in mind 
    that each 'line' of this file represents a unique document 
    that we wish to classify. Fill in the missing code to get
    the probability of each class given the words in the document.
    Remember that you will need to handle the case where you
    encounter a word that is not represented in the model.
"""
import os
import re
import sys
import numpy as np

# confirm that we have access to the model file
assert 'NBmodel.txt' in os.listdir('.'), "ERROR: can't find NBmodel.txt"

# load the model into a dictionary for easy access
MODEL = {}
for record in open('NBmodel.txt', 'r').readlines():
    word, payload = record.split('\t')
    # extract conditional probabilities
    ham_cProb, spam_cProb = payload.split(',')[2:]
    # save their logs as a tuple in our model dictionary
    take_log = lambda x: np.log(x) if x != 0 else float("-inf")
    MODEL[word] = (take_log(float(ham_cProb)),
                   take_log(float(spam_cProb)))

# read from standard input
for line in sys.stdin:
    # parse input and tokenize
    docID, _class, subject, body = line.lower().split('\t')
    words = re.findall(r'[a-z]+', subject + ' ' + body)
    # initialize variables that student code should overwrite
    logpHam, logpSpam, pred_class = None, None, None
    
    ################# YOUR CODE HERE ################
    # TIP: try using MODEL.get(word, (0,0)) to access the tuple 
    # of log probabilities without throwing a KeyError!

    #initializing scores w/ only class prior (no terms). [0] is ham index(ie. not China). [1] is spam index (ie. China) 
    logpHam = MODEL.get('ClassPriors',(0,0))[0] 

    logpSpam = MODEL.get('ClassPriors',(0,0))[1]

    #Ham
    for term in words: #each word in doc. 
        if term not in MODEL.keys():
            continue
        if term == 'ClassPriors':
            continue
        else: #Only execute if term in document. 
            logpHam += MODEL.get(term,(0,0))[0] #0 for Ham

    #Spam
    for term in words: #each word in doc.
        if term not in MODEL.keys():
            continue
        if term == 'ClassPriors':
            continue
        else: #Only execute if term in document. 
            logpSpam += MODEL.get(term,(0,0))[1] #1 for Spam

    if logpHam < logpSpam:
        pred_class = 1
    else:
        pred_class = 0


    ################# (END) YOUR CODE ##############
#  UNCOMMENT  
    print(f"{docID}\t{_class}\t{logpHam}\t{logpSpam}\t{pred_class}")
