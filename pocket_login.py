from pocket import Pocket
import requests
import webbrowser
import oauth_http_server

class PocketLogin(object):

	def __init__(self, consumer_key):
		self.consumer_key = consumer_key
		self.request_Token = None
		self.access_token = None

	def login(self):
		auth_server = oauth_http_server.OAuthServer(callback=self.handle_oauth_callback)
		self.request_token = Pocket.get_request_token(self.consumer_key, redirect_uri=auth_server.get_oauth_callback_url())
		login_url = Pocket.get_auth_url(self.request_token, redirect_uri=auth_server.get_oauth_callback_url())
		webbrowser.open(login_url)
		auth_server.serve_forever()
		return self.access_token

	def handle_oauth_callback(self, data):
		self.access_token = Pocket.get_access_token(self.consumer_key, self.request_token)

