import cgi
from google.appengine.api import users
import webapp2
from __builtin__ import str

MAIN_PAGE_HTML = """\
<html>
  <body>
    Enter password to check and click on Submit: 
    <form action="/check" method="post">
      <div><textarea name="content" rows="1" cols="60"></textarea></div>
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
        password = self.request.get('content')
        
        ###
        # TODO: Put your code here that performs the tests on the password, as per example line below
        ##/
        hasUpperAndLower = not password.isupper() and not password.islower()
        
        self.response.write('<html><body>Password Check Results:<pre>')
        self.response.write('(a) Has at least one uppercase and one lowercase character - ' + str(hasUpperAndLower) + '\n')
        
        ###
        # TODO: write the rest of the results of the tests here (using example above)
        ##/
        
        self.response.write('Your password strength is: ' + 'Strong\n') # TODO modify this so that the final result is not hard-coded
        self.response.write('</pre></body></html>')

application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/check', PWChecker),
], debug=True)
