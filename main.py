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
import os
import cgi
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.api import users
from google.appengine.ext.webapp import template
from google.appengine.ext import db

from models.model import Post
from views.view import Postador

class MainHandler(webapp.RequestHandler):
    def get(self):
		user = users.get_current_user()
		
		if user:
			posts = db.GqlQuery("select * from Post order by date desc limit 10")
			template_values = {"user_nickname": user.nickname(),
								"posts" : posts,
								"logout_url": users.create_logout_url('/')}
			path = os.path.join(os.path.dirname(__file__),'templates/index.html')
			self.response.out.write(template.render(path,template_values))	
		else:
			self.redirect(users.create_login_url(self.request.uri))
			

application = webapp.WSGIApplication([('/', MainHandler)],
                                         debug=True)	

def main():
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
