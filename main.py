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
from google.appengine.api import mail
from google.appengine.api import users



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
    template = JINJA_ENVIRONMENT.get_template('templates/contact.html')

    def get(self):
        self.response.out.write(self.template.render())

    # def post(self):
    #     # takes input from user
    #     userMail = self.request.get("mail")
    #     subject = self.request.get("subject")
    #     name = self.request.get("name")
    #     userMessage = self.request.get("message")
    #     message = mail.EmailMessage(sender=userMail, subject=subject)

    #     # not tested
    #     if not mail.is_email_valid(userMail):
    #         self.response.out.write("Wrong email! Check again!")

    #     message.to = "jingwa@umich.edu"
    #     message.body = """Thank you!
    #         You have entered following information:
    #         Your mail: %s
    #         Subject: %s
    #         Name: %s
    #         Message: %s""" % (userMail, subject, name, userMessage)
    #     message.send()
    #     self.response.out.write("Message sent!")


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/index', MainHandler),
    ('/resume', MainHandler),
    ('/gallery', MainHandler),
    ('/contact', ContactHandler)
], debug=True)
