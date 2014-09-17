import json
import os
import urllib

import jinja2
import webapp2
from deseret import Deseret

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

globals = {}


class MainPage(webapp2.RequestHandler):

        
    def post(self):
        d = globals.get('deseret', None);
        if not d:
            print "Globals were not initialized. Initializing now..."
            d = Deseret()
            globals['deseret'] = d

        text = self.request.get('input_text')

        #print "text = %s" % text
        if text:
            deseret_text = d.translate(text)
        else:
            deseret_text = ""

        template_values = {
            "input_text": text,
            "output_text": deseret_text
        }

        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))


    def get(self):
        self.post()

class WarmupHandler(webapp2.RequestHandler):

    def get(self):
        print "Warming up..."
        d = globals.get('deseret', None)
        if not d:
            globals['deseret'] = Deseret()
        print "Done warming up."
        self.response.write("All warmed up!")

application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/_ah/warmup', WarmupHandler)
], debug=True)
