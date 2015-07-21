#---------------------------------------------------------
# April Dawn Kester
# akester@ischool.berkeley.edu
# Homework #5
# October 1, 2014
# BST - Client
#---------------------------------------------------------

from BST import *
from hw5.kester import *


##On final test of file, carage return is being added to word count >.<
#used len(word) >0 to fix, had to parse out \xef\xbb\xbf


##Initial testing of main file
#test = "testing... removal!! of %$*^punctuation and 6753digits new words white space CHANGE TO LOWERCASE"
#test = stripItAll(test)
#print test
#
#with open('test.txt','r') as file:
#    for line in file:
#        for word in line.split():
#            word = stripItAll(word)
#            print(word)

##tested with personal test.txt files of various length (encluding empty file), sample snipit from assignment and then using test_file.txt ebook linked in assignment

##Initial testing of Node constructor and functions
#r = Node("hello")
#_add(r, "goodbye")
#_add(r, "april")
#_add(r, "goodbye")
#_add(r, "goodbye")
#_add(r, "hello")
#
#print "in order:"
#_inOrderPrint(r)
#
#f = _find(r, "goodbye")
#print f.word
#print f.count
#
#f = _find(r, "april")
#print f.word
#print f.count
#
#f = _find(r, "hello")
#print f.word
#print f.count

##Initial testing of BSTree constructor and functions
#T = BSTree()
#T.add("goodbye")
#T.add("april")
#T.add("hello")
#T.add("april")
#
#T.inOrderPrint()
#print T.height()
#
#Needle = T.find("april")
#print Needle.word
#print Needle.count
#
#Needle = T.find("notfound")  #NEED TO HANDLE THIS - FIXED
#print Needle.word
#print Needle.count
#
#print T.size()
#
#T.add("candy")
#T.add("can")
#T.add("summer")
#
#print T.size()
#print T.height()
#
#
#T.add("can")
#T.add("summer")
#T.add("april")
#
#Needle = T.find("april")
#print Needle.word
#print Needle.count
#
#print T.height()








