#---------------------------------------------------------
# April Dawn Kester
# akester@ischool.berkeley.edu
# Homework #5
# October 1, 2014
# test
#---------------------------------------------------------

import urllib2
import re
import string


Words = {}

url = "http://people.ischool.berkeley.edu/~tygar/for.i206/pg1342.txt"

req = urllib2.Request(url)
response = urllib2.urlopen(req)
for line in response:
    for word in line.split():
        wordLength = len(word)
        if wordLength > 0:
            Words[word] = [1]

print Words