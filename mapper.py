from collections import OrderedDict
import string
import re
import sys
spec_words = ["is", "on", "the"]
# input comes from STDIN (standard input)
for line in sys.stdin:
    #remove numbers from text
    line = re.sub(r'\d+', '', line)
    #convert all to lower case
    line = line.lower()
    #remove the punctuation
    table = line.maketrans({}.fromkeys(string.punctuation))
    line = line.translate(table)
    # remove leading and trailing whitespace
    line = line.strip()
    #remove extra punc
    line = line.replace('—','')
    line = line.replace('’','')
    line = line.replace('“','')
    line = line.replace('”','')
    # split the line into words
    words = line.split()
    # increase counters
    #print("-----------------------Mapper.py output-----------------------")


    for i in range(len(words)-2):
        terms = OrderedDict()
        dollar_count = 0
        for j in range(3):
            if words[i+j] in spec_words:
                terms[words[i+j]] = '$'
                dollar_count += 1
            else:
                terms[words[i + j]] = words[i+j]
        if dollar_count == 1:
            vals = list(terms.values())
            print('%s_%s_%s\t%s' %(vals[0], vals[1], vals[2],1))
        else:
            keys = list(terms.keys())
            for k in range(len(keys)):
                vals = []
                if terms[keys[k]] == '$':
                    for l in range(3):
                        if l == k:
                            vals.append('$')
                        else:
                            vals.append(keys[l])
                    print('%s_%s_%s\t%s' % (vals[0], vals[1], vals[2],1))




