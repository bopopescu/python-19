#---------------------------------------------------------
# April Dawn Kester
# akester@ischool.berkeley.edu
# INFO 206 Homework #2
# September 12, 2014
# README
# Password strength checker README file
#---------------------------------------------------------

Table of content:
hw2.instructions
hw2.kester.py 
hw2.ec.kester.py 
passwords common
README

Special instructions:
Checks user input password, determines if it meets conditions and compares it to a list of common passwords
Type finish to end the program

Please enter your password: baby

Your Password is VERY WEAK!

Conditions Your Password Must Meet
CONDITION NOT MET: It has at least one uppercase and at least one lowercase letter 
CONDITION NOT MET: It has at least one digit 
CONDITION NOT MET: It has at least one character that is not a letter or a digit 
CONDITION NOT MET: It has a length of at least six characters 

Total times this algorithm makes a comparison:  12
Your password FAILED, it is on the list

Additional information:
The binary search algorithm counter seems to be accurate for smaller values of n, but not so much for the list of 10,000.  

For this section I was able to use the getpass() function to keep the program from echoing what the user types to the console.  It is possible to modify this function to echo an asterisk, but it appears interactive input editing is OS dependent.

The recursive algorithm does not have a counter.

Final Grade:
9.5/10

Comments:
Use the strip() function to clean up the '\n' characters from the file; if you are going to test using internal functions, make sure you do sanity tests with real input as well; You should also test boundary cases such as the first, last, and middle password on the list; bonus 0.5 pts input mask!; bonus 0.5 pts recursive algo!; you do not print out number of comparisons for recursive algo