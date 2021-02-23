from operator import itemgetter
import sys
from collections import OrderedDict

current_word = None
current_count = 0
word = None
dic = {}
for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t', 1)
    try:
        count = int(count)
    except ValueError:
        continue

    if current_word == word:
        current_count += count
    else:
        if current_word:
            dic[current_word] = current_count
        current_count = count
        current_word = word


if current_word == word:
    dic[current_word] = current_count

sorted_dic = OrderedDict(sorted(dic.items(), key=itemgetter(1), reverse=True))

count = 0
for key in sorted_dic.keys():
    if count < 10:
        print ('%s\t%s' % (key, sorted_dic[key]))
        count+=1
    else:
        break


