import os
import urllib
import logging

import jinja2
import webapp2
from webapp2_extras import json

from deseret import Deseret

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

def get_global_deseret():

    app = webapp2.get_app()
    d = app.registry.get('deseret')
    if not d:
        print "Globals were not initialized. Initializing now..."
        d = Deseret()
        app.registry['deseret'] = d

    return d


class MainPage(webapp2.RequestHandler):

    def post(self):
        d = get_global_deseret()

        english = self.request.params.get('english')

        #print "english = %s" % english
        if english:
            deseret = d.translate(english)
        else:
            deseret = ""

        template_values = {
            "english": english,
            "deseret": deseret
        }

        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))


    def get(self):
        self.post()


class WarmupHandler(webapp2.RequestHandler):

    def get(self):
        print "Warming up..."
        get_global_deseret()
        self.response.write("All warmed up!")

class JsonHandler(webapp2.RequestHandler):

    def post(self):

        json_obj = json.decode(self.request.body)
        english = json_obj['english']

        d = get_global_deseret()
        deseret = d.translate(english)
        self.response.content_type = 'application/json'
        obj = {
            'deseret': deseret
        } 
        self.response.write(json.encode(obj))


def handle_error(request, response, exception):
    logging.exception(exception)
    error_code = 500
    error_description = str(exception)
    if isinstance(exception, webapp2.HTTPException):
        error_code = exception.code
        error_description = exception.explanation

    response.status = error_code

    if request.path.startswith('/json'):
        response.headers.add_header('Content-Type', 'application/json')
        result = {
            'status': 'error',
            'status_code': error_code,
            'error_message': error_description,
          }
        response.write(json.encode(result))
    else:
        response.write(error_description)


application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/_ah/warmup', WarmupHandler),
    ('/json/translation', JsonHandler),
], debug=True)
application.error_handlers[404] = handle_error
application.error_handlers[400] = handle_error
application.error_handlers[500] = handle_error
