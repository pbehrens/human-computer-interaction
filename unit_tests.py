import unittest
import twitter
import MuchOAuthenticator
import sys

class TestMuchOAuthenticator(unittest.TestCase):

	api = None

	def setUp(self):
		try:
			self.api = MuchOAuthenticator.getAuthenticatedApi()
		except twitter.TwitterError,e:
			print "Error:", str(e)
			self.fail("getAuthenticatedApi() failed!")

	def test_verifyApi(self):
		try:
			verification = self.api.VerifyCredentials()
			print verification
		except twitter.TwitterError,e:
			print "Error:", str(e)
			self.fail("Could not authenticate api!")

if __name__ == '__main__':
	unittest.main()
