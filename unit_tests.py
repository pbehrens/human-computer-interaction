import unittest
import twitter
import twitteroauth
import sys
from outputcontroller import OutputController
from worddictionary import WordDictionary

class TestMuchOAuthenticator(unittest.TestCase):
    api = None
    def setUp(self):
        try:
            self.api = twitteroauth.getAuthenticatedApi()
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

    def test_wordDictionary(self):
        wordDict = WordDictionary()
        self.assertTrue(len(wordDict.getHappy()) > 0)
        self.assertTrue(len(wordDict.getSad()) > 0)
        self.assertTrue(len(wordDict.getAngry()) > 0)
        self.assertTrue(len(wordDict.getProfane()) > 0)


if __name__ == '__main__':
	unittest.main()
