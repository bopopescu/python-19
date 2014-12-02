#---------------------------------------------------------
# April Dawn Kester
# akester@ischool.berkeley.edu
# INFO 206 Homework #2
# September 12, 2014
# hw2.kester.py
# Password strength checker
#---------------------------------------------------------

import sys
import re

conditions = [] #initializing conditions [boolean] array
password_list = [] #initializing password [string] array

def check_uppercase(pw): #checking for an uppercase letter
    return any(char.isupper() for char in pw)

def check_lowercase(pw): #checking for a lowercase letter
    return any(char.islower() for char in pw)

def check_cases(pw): #returns true if there are upper and lowercase letters
    return bool(check_uppercase(pw) == 1 & check_lowercase(pw) == 1)

def check_digit(pw): #checking for a digit
    return any(char.isdigit() for char in pw)

def check_other(pw, search=re.compile(r'[^A-Za-z0-9]').search): #checking for other
    return bool(search(pw))

def check_length(pw): #checking length at least 6
    return bool(len(pw) >= 6)

def check_conditions(conditions): #counting conditions met
    return conditions.count(1)

def search(pw, password_list): #search password list for user password
    counter = 0
    low = 0
    high = len(password_list) -1
    while low <= high:
        mid = (low + high)/2
        item = password_list[mid]
        if pw == item:
            print "Total times this algorithm makes a comparison: ", counter
            return counter
        elif pw < item:
            high = mid -1
        else:
            low = mid +1
        counter +=1
        #I am only printing from this function because you specifically asked for the counter
    print "Total times this algorithm makes a comparison: ", counter
    return -1


################      MAIN       #####################

#retrieving list of passwords from file
file = open("passwords common.txt", mode="U")
for line in file:
    password_list.append(line)
file.close()


#infinite loop
var = 1
while var == 1:
    pw = raw_input("Please enter your password: ")
    #print pw
    if pw == "finish":
        print "Goodbye!"
        sys.exit()

    #check conditions, save to array
    conditions.append(check_cases(pw))
    conditions.append(check_digit(pw))
    conditions.append(check_other(pw))
    conditions.append(check_length(pw))
    #print conditions #DEBUG

    conditions_count = check_conditions(conditions)
    #print conditions_count #DEBUG

    new_pw = pw.lower()
    new_pw += "\n"

    #print len(password_list) #DEBUG
    #print password_list #DEBUG

    #print to terminal strength of password
    print ""
    if conditions_count == 0:
        print "Your Password is VERY WEAK!"
    elif conditions_count == 1:
        print "Your Password is WEAK"
    elif conditions_count == 2:
        print "Your Password is MEDIUM"
    elif conditions_count == 3:
        print "Your Password is HIGH MEDIUM"
    elif conditions_count == 4:
        print "Your Password is STRONG!"
    else:
        print "Something went very very wrong"

    #print to terminal specific conditions met
    print ""
    print "Conditions Your Password Must Meet"
    if conditions[0] == 1:
        pass_fail = "CONDITION MET:"
    else:
        pass_fail = "CONDITION NOT MET:"
    print pass_fail, "It has at least one uppercase and at least one lowercase letter "

    if conditions[1] == 1:
        pass_fail = "CONDITION MET:"
    else:
        pass_fail = "CONDITION NOT MET:"
    print pass_fail, "It has at least one digit "

    if conditions[2] == 1:
        pass_fail = "CONDITION MET:"
    else:
        pass_fail = "CONDITION NOT MET:"
    print pass_fail, "It has at least one character that is not a letter or a digit "

    if conditions[3] == 1:
        pass_fail = "CONDITION MET:"
    else:
        pass_fail = "CONDITION NOT MET:"
    print pass_fail, "It has a length of at least six characters "

    print ""
    if search(new_pw, password_list) == -1:
        print "Your password is NOT on the list"
    else:
        print"Your password FAILED, it is on the list"

    print ""
    conditions[:] = []

