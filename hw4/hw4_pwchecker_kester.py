#---------------------------------------------------------
# April Dawn Kester
# akester@ischool.berkeley.edu
# Homework #4
# September 26, 2014
# Password strength checker for GoogleAppEngine
#---------------------------------------------------------

import cgi
from google.appengine.api import users
import webapp2
from __builtin__ import str
import sys
import re
import getpass

MAIN_PAGE_HTML = """\
<html>
  <body>
    <BODY BGCOLOR="E6E6FA" TEXT="4B0082">
    <h1>Welcome to April Dawn's Password Check App!!</h1>
    Please enter a password to check and click on <b>Submit</b>:
    <form action="/check" method="post">
      <div><textarea name="content" rows="2" cols="60"></textarea></div>
      <div><input type="submit" value="Submit"></div>
    </form>
  </body>
</html>
"""

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write(MAIN_PAGE_HTML)

class PWChecker(webapp2.RequestHandler):
    def post(self):
        
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
        
        def search_recursive(password_list, pw, low, high): #search password list for user password
            if (high < low):
                return -1
            else:
                mid = low + ((high - low) /2)
                if pw == password_list[mid]:
                    return mid
                elif (password_list[mid] > pw):
                    return search_recursive(password_list, pw, low, mid-1)
                else:
                    return search_recursive(password_list, pw, mid+1, high)
    
        
        #retrieving list of passwords from file
        file = open("passwords common.txt", mode="U")
        for line in file:
            password_list.append(line)
        file.close()
        
        pw = self.request.get('content')
        
        #check conditions, save to array
        conditions.append(check_cases(pw))
        conditions.append(check_digit(pw))
        conditions.append(check_other(pw))
        conditions.append(check_length(pw))
        
        conditions_count = check_conditions(conditions)
        
        new_pw = pw.lower()
        new_pw += "\n"
            
        #print to terminal strength of password
        self.response.write('<html><body><BODY BGCOLOR="E6E6FA" TEXT="4B0082"> <h2>Password Check Results:</h2><pre>')
        if conditions_count == 0:
            self.response.write('Your Password is VERY WEAK!\n')
        elif conditions_count == 1:
            self.response.write('Your Password is WEAK\n')
        elif conditions_count == 2:
            self.response.write('Your Password is MEDIUM in strength\n')
        elif conditions_count == 3:
            self.response.write('Your Password is HIGH MEDIUM in strength\n')
        elif conditions_count == 4:
            self.response.write('Your Password is STRONG!\n')
        else:
            self.response.write('Something went very very wrong\n')
                
        #print to terminal specific conditions met
        self.response.write('\n')
        self.response.write('Conditions Your Password Must Meet:\n\n')
        if conditions[0] == 1:
            pass_fail = "CONDITION MET: "
        else:
            pass_fail = "CONDITION NOT MET: "
        self.response.write(str(pass_fail) + 'It has at least one uppercase and at least one lowercase letter \n')
        
        if conditions[1] == 1:
            pass_fail = "CONDITION MET: "
        else:
            pass_fail = "CONDITION NOT MET: "
        self.response.write(str(pass_fail) + 'It has at least one digit \n')
        
        if conditions[2] == 1:
            pass_fail = "CONDITION MET: "
        else:
            pass_fail = "CONDITION NOT MET: "
        self.response.write(str(pass_fail) + 'It has at least one character that is not a letter or a digit \n')
        
        if conditions[3] == 1:
            pass_fail = "CONDITION MET: "
        else:
            pass_fail = "CONDITION NOT MET: "
        self.response.write(str(pass_fail) + 'It has a length of at least six characters \n')
        
        self.response.write('\n')
        if search_recursive(password_list, new_pw, low=0, high=len(password_list) -1) == -1:
            self.response.write('Good job! Your password is NOT on the list of most common passwords, please hit the browser back button to try again.')
        else:
            self.response.write('Your password FAILED, it is on the list of most common passwords, please hit the browser back button to try again.')
        conditions[:] = []


        self.response.write('\n')
        self.response.write('</pre></body></html>')



application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/check', PWChecker),
], debug=True)


