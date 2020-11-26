#!/usr/bin/env python
"""
This script reads word counts from STDIN and aggregates
the counts for any duplicated words.

INPUT & OUTPUT FORMAT:
    word \t count
USAGE (standalone):
    python aggregateCounts_v2.py < yourCountsFile.txt

Instructions:
    For Q7 - Your solution should not use a dictionary or store anything   
             other than a single total count - just print them as soon as  
             you've added them. HINT: you've modified the framework script 
             to ensure that the input is alphabetized; how can you 
             use that to your advantage?
17 is where docstring should end
delete
c) code: Write the main part of aggregateCounts_v2.py so that it takes advantage of the sorted input to add duplicate counts without storing the whole vocabulary in memory. Refer to the file docstring for more detailed instructions. Confirm that your implementation works by running it on both the test and true data files.


# imports
import sys
from collections import defaultdict

########### PROVIDED IMPLEMENTATION ##############  

counts = defaultdict(int)
# stream over lines from Standard Input
for line in sys.stdin:
    # extract words & counts
    word, count  = line.split()
    # tally counts
    counts[word] += int(count)
# print counts
for wrd, count in counts.items():
    print("{}\t{}".format(wrd,count))
    
########## (END) PROVIDED IMPLEMENTATION #########

/delete

"""

# imports
import sys
from collections import defaultdict


################# YOUR CODE HERE #################
word = 'qzq' #intializing var with placeholder word not likely to actually occur.
count = 0 #initilizing var with placeholder

# stream over lines from Standard Input
#print('aaaahoohoo',"\t","99999")
for line in sys.stdin:
    # extract words & counts
    prior_word = word #from prior iteration or initialization
    prior_count = count #from prior iteration or initializion
    if prior_word == line.split()[0]: #case of prior & current word match
        word = prior_word
        count = prior_count + int(line.split()[1])
        continue
    else: #case of prior & current word do not match
        word = line.split()[0]
        count = int(line.split()[1])
        if prior_word == 'qzq': #1st iteration only
            continue
        else:
            #print counts (from prior iteration)
            print(prior_word,"\t",prior_count)
print(word,"\t",count)   #last iteration      
#     print(line.split()[0], "\t", line.split()[1])
################ (END) YOUR CODE #################
