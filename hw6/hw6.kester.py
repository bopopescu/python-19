#---------------------------------------------------------
# April Dawn Kester
# akester@ischool.berkeley.edu
# Homework #6
# October 10, 2014
# SE
#---------------------------------------------------------
import sys
import urllib2
import re
import string
from collections import defaultdict

#must indicate number of files in the catalog
number = 10

# Phase 1
# Books dictionary
# Key: currentline[0] = book title
# Value list: seq starting at 0, currentline[1] = URL
Books = {}

# Titles list
# Titles in order
Titles = []

#open file
filename = "catalog.txt"
try:
    with open(filename, mode="U") as file:
        bookID = 0
        for line in file:
            currentline = line.split(",")
            if len(currentline) != 2:
                print "Your file is not properly formated"
                print "Goodbye!"
                sys.exit()
            Books [currentline[0]] = [bookID, currentline[1].strip("\n")]
            Titles.append(currentline[0]) #SOLVE FOR DUPLICATES
            bookID += 1
            #print bookID

    file.close()
except IOError:
    print "Can not open", filename
    print "Goodbye!"
    sys.exit()

#print Books #Does not print in order
#print Titles

# Phase 2
# Parse words of all the crap, from HW5
def stripItAll(test):
    re.sub(r'\W+', '', test)
    test = test.rstrip('\r\n')
    test = ''.join([i for i in test if not i.isdigit()])
    test = test.translate(string.maketrans("",""), string.punctuation)
    test = test.lower()
    return test


# Words dictionary
# Key: word
# Value: WordCounts
Words = defaultdict(list)

# read from Books dictinary for URL
# k = book title, v[0] = bookID, v[1] = URL
for k, v in Books.iteritems():
    #print k, v[0], v[1]
    bookID = v[0]
    url = v[1]
    req = urllib2.Request(url)
    try: response = urllib2.urlopen(req)
    except (ValueError,urllib2.URLError):
        print "Problem fetching URL"
        print "Goodbye!"
        sys.exit()
    for line in response:
        for word in line.split():
            word = stripItAll(word)
            wordLength = len(word)
            if wordLength > 0:


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



# Phase 3


def findTitles(bookLookUp, Titles):
    for n, item in enumerate(Titles):
        if n == bookLookUp:
            return item

def findBook(bookLookUp, Books):
    for k, v in Books.iteritems():
        if v[0] == bookLookUp:
            toPrint = k, v[1]
            return toPrint


# infinite loop
var = 1
while var == 1:
    print "Query?"
    input = raw_input()
    searchWord = stripItAll(input) 
    if searchWord == "catalog":
        for k, v in sorted(Books.iteritems()):
            print k,":[",v[0],",",v[1],"]"
    elif searchWord == "titles":
        for books in Titles:
            print books
    elif searchWord == "terminate":
        print "Goodbye!"
        sys.exit()
    elif (Words.has_key(searchWord) == False):
        print "The word", searchWord, "does not appear in any book in the library"
    else:
        #print Words[searchWord]
        # GIVES ME LIST OF CONTS BASED OFF INDEX POSITION
        myList = Words.get(searchWord)
        myCount = 1
        
        for n, item in enumerate(myList):
            myList[item] = [item, n]
            
            if item == 1:
                plural = "time"
            else:
                plural = "times"
            if item > 0:
                
                t = findBook(n, Books)
                print myCount,". The word", searchWord, "appears",item, plural,"in",t
                myCount +=1


#It should report books sorted in the order of how many times a word appears in the book








