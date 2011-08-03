import cgi

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.api import users
from google.appengine.ext import db
from models.model import Post


class Postador (webapp.RequestHandler):
	def post(self):
		post = Post()
		if users.get_current_user():
			post.author = users.get_current_user()
		post.title = cgi.escape(self.request.get('title'))
		post.content = cgi.escape(self.request.get('content'))
		post.put()
		self.redirect('/')
	
		
class Deletor (webapp.RequestHandler):
	def post(self):
		post_key = cgi.escape(self.request.get('post_key'))
		p = db.get(post_key)
		p.delete()
		self.response.out.write('deletado')
	

		

application = webapp.WSGIApplication([('/postar', Postador),
										('/post/delete', Deletor)],
                                         debug=True)
   
def main():
    util.run_wsgi_app(application)
		
if __name__ == '__main__':
    main()

		