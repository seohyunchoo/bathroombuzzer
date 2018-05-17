import webapp2
import jinja2

import os

from google.appengine.ext import ndb

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True
)

class Person(ndb.Model):
    name = ndb.StringProperty
    num_times = ndb.IntegerProperty

class MainPage(webapp2.RequestHandler):
    def get(self):
        number = 3
        template_values = {
            'name': "Roberto",
            'num_times': number,
        }

        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))

class Reportbook(webapp2.RequestHandler):
    def post(self):
        print 'Report was received'
        self.redirect('/')

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/report', Reportbook),
], debug=True)
