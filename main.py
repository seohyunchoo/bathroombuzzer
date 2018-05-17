import webapp2
import jinja2

import os

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True
)

class MainPage(webapp2.RequestHandler):
    def get(self):
        number = 3
        template_values = {
            'number': number,
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
