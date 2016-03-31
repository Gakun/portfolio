#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import os
import jinja2
import logging


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class MainHandler(webapp2.RequestHandler):
    def get(self):
        path = self.request.path
        try:
            template = JINJA_ENVIRONMENT.get_template('templates' + path + '.html')
        except:
            template = JINJA_ENVIRONMENT.get_template('templates/index.html')

        if path == '/' or path == '/index':
            self.response.write(template.render({"title": "Home"}))
        elif path == '/resume':
            self.response.write(template.render({"title": "Resume"}))
        elif path == '/gallery':
            self.response.write(template.render({"title": "Gallery"}))


class ContactHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/contact.html')
        self.response.write(template.render({"title": "contact"}))

    def post(self):
        user = self.request.get('name')
        pw = self.request.get('pw')
        logging.info("POST: Input username is " + user)
        logging.info("POST: Input password is " + pw)
        if user == 'Colleen' and pw == "pass":
            template = JINJA_ENVIRONMENT.get_template('templates/loginsuccess.html')
            self.response.write(template.render({"title": "Login"}))
        else:
            msg = 'Bad credentials. Try again.'
            template = JINJA_ENVIRONMENT.get_template('templates/login.html')
            self.response.write(template.render({"title": "Login", "msg": msg}))


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/index', MainHandler),
    ('/resume', MainHandler),
    ('/gallery', MainHandler),
    ('/contact', ContactHandler)
], debug=True)
