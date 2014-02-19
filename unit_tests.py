import unittest
import twitter
import muchoauth
import sys
from outputcontroller import OutputController

class TestMuchOAuthenticator(unittest.TestCase):
    api = None
    def setUp(self):
        try:
            self.api = muchoauth.getAuthenticatedApi()
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
    
    def test_verifyColorOutput(self):
        outControl = OutputController()
        outputedColor = outControl.outputColor("red")
        self.assertEqual(outputedColor, "red")
    
    def test_getCurrentColor(self):
        outControl = OutputController()
        outputedColor = outControl.outputColor("red")
        self.assertEqual(outputedColor, "red")
        
        currentColor = outControl.getCurrentColor()
        self.assertEqual(currentColor, "red")
        

if __name__ == '__main__':
	unittest.main()
