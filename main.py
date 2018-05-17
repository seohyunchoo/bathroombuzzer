import webapp2
import jinja2

import os

from google.appengine.ext import ndb

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True
)

class Badguy(ndb.Model):
    name = ndb.StringProperty()
    number = ndb.IntegerProperty()

class MainPage(webapp2.RequestHandler):
    def get(self):
        badguy_query = Badguy.query()

        template_values = {
            'badguy_list': badguy_query.fetch(),
        }

        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))

class Report(webapp2.RequestHandler):
    def post(self):
        print 'Report was received'
        print self.request.GET["badguy_name"]
        badguy_query = Badguy.query(Badguy.name == self.request.GET['badguy_name'])
        badguy = badguy_query.fetch()[0]
        badguy.number += 1
        badguy.put()
        self.redirect('/')

class AddNewPerson(webapp2.RequestHandler):
    def post(self):
        new_person = Badguy( name = self.request.get('name'), number = 1 )
        new_person.put()
        self.redirect('/')

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/report', Report),
    ('/addperson', AddNewPerson),
], debug=True)
