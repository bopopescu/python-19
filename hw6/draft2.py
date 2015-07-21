#---------------------------------------------------------
# April Dawn Kester
# akester@ischool.berkeley.edu
# Homework #6
# October 10, 2014
# test 2
#---------------------------------------------------------

from collections import defaultdict
number = 5
bookID = 1

Words = defaultdict(list)

response = "once upon a time there was a grey cat he was cool and there was once a blue cat he was not cool"
words = response.split()
for word in words:


        #check to see if word exists in dictionary
    if Words.has_key(word):
        myList = Words.get(word)
    
    
        #if word exists check to see if book exists
        for n, item in enumerate(myList):
            #print n, item
            
            #for index, item in enumerate(myList):
            if n == bookID:
    
                #if book exists +1 to word count
                item += 1
                myList.pop(n)
                myList.insert(n, item)
                Words[word] = myList

        #if word does not exist in dictionary - add word to dictinary
    else:
        WordsCount = [0] * number
        WordsCount.pop(bookID)
        WordsCount.insert(bookID, 1)
        Words[word] = WordsCount

for k, v in Words.iteritems():
#print k, v
    myList = Words.get(k)
    print myList


