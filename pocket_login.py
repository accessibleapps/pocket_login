from urllib import quote_plus
from pocket import Pocket
import requests
import webbrowser
import oauth_http_server

class PocketLogin(object):

	def __init__(self, consumer_key):
		self.request_Token = None
		self.access_token = None
		self.pocket = Pocket(consumer_key)

	def get_auth_url(self, request_token, redirect_url):
		return 'https://getpocket.com/auth/authorize?request_token={request_token}&redirect_uri={redirect_url}'.format(
			request_token = quote_plus(request_token),
			redirect_url = quote_plus(redirect_url),
		)


	def login(self):
		auth_server = oauth_http_server.OAuthServer(callback=self.handle_oauth_callback)
		self.request_token = self.pocket.get_request_token(redirect_url=auth_server.get_oauth_callback_url())
		login_url = self.get_auth_url(self.request_token, redirect_url=auth_server.get_oauth_callback_url())
		webbrowser.open(login_url)
		auth_server.serve_forever()
		return self.access_token

	def handle_oauth_callback(self, data):
		self.access_token = self.pocket.get_access_token(self.request_token)

