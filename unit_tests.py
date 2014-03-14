import unittest
import twitter
import twitteroauth
import sys
from outputcontroller import OutputController
from worddictionary import WordDictionary
from gui import Gui

class TestMuchOAuthenticator(unittest.TestCase):

    api = None
    gui = None

    def setUp(self):
        try:
            #TODO Uncomment to test Twitter oAuth
            #self.api = twitteroauth.getAuthenticatedApi()
            self.gui = Gui()
        except twitter.TwitterError,e:
			print "Error:", str(e)
			self.fail("getAuthenticatedApi() failed!")
	
	def test_verifyApi(self):
		try:
            #TODO Uncomment to test Twitter credentials
			#verification = self.api.VerifyCredentials()
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

    def test_gui(self):
        self.assertEqual(self.gui.color, 'white')
        self.gui.setColor('red')
        self.assertEqual(self.gui.color, 'red')

if __name__ == '__main__':
	unittest.main()
