#---------------------------------------------------------
# April Dawn Kester
# akester@ischool.berkeley.edu
# Homework #5
# October 1, 2014
# Main File
#---------------------------------------------------------

from BST import *
import re
import string
import sys
from sys import argv


def stripItAll(test):
    re.sub(r'\W+', '', test)
    test = test.rstrip('\r\n')
    test = ''.join([i for i in test if not i.isdigit()])
    test = test.translate(string.maketrans("",""), string.punctuation)
    test = test.lower()
    return test


def main():

    T = BSTree()
    
    filename = argv
    print "Enter the file name to read:"
    filename = raw_input("> ")
    
    try:
        with open(filename, mode="U") as file:
            file.read(3)
            for line in file:
                for word in line.split():
                    word = stripItAll(word)
                    wordLength = len(word)
                    if wordLength > 0:
                        T.add(word)
        file.close()
    except IOError:
        print "Can not open", filename
        print "Goodbye!"
        sys.exit()
    
    #T.inOrderPrint()
    
    #infinite loop
    var = 1
    while var == 1:
        print "Query?"
        searchWord = raw_input()
        if searchWord == "stats":
            print "Elements in this tree: ", T.size()
            print "Depth of this tree: ", T.height()
        elif searchWord == "terminate":
            print "Goodbye!"
            sys.exit()
        else:
            Needle = T.find(searchWord)
            if Needle == -1:
                print "Word Not Found"
            else:
                print "The word ", Needle.word, " appears ", Needle.count, " times in the tree"

if __name__ == "__main__":
    main()  





