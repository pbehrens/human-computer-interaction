import unittest
import twitter
import twitteroauth
import sys
from outputcontroller import OutputController
from worddictionary import WordDictionary
from gui import Gui
from word import Word
from document import Document
from doc_queue import DocQueue

# Place holder function for gui init
def placeHolder():
    return 0

class TestMuchOAuthenticator(unittest.TestCase):

    api = None
    gui = None

    def setUp(self):
        try:
            #TODO Uncomment to test Twitter oAuth
            #self.api = twitteroauth.getAuthenticatedApi()
            self.gui = Gui(placeHolder)
        except twitter.TwitterError,e:
            print "Error:", str(e)
            self.fail("getAuthenticatedApi() failed!")

    def test_verifyApi(self):
        try:
            #TODO Uncomment to test Twitter credentials
            #verification = self.api.VerifyCredentials()
            #print verification
            print "nothing"
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

    def test_word(self):
        word = Word("test")
        self.assertEqual(word.getName(), "test")
        word.setTF(0.4)
        word.setIDF(0.6)
        self.assertEqual(word.getTF(), 0.4)
        self.assertEqual(word.getIDF(), 0.6)

    def test_document(self):
        word = Word("test")
        word.setTF(0.4)
        word.setIDF(0.6)
        doc = Document("hello my name is")
        self.assertEqual(doc.getDocString(), "hello my name is")
        doc.addRealWord(word)
        self.assertEqual(doc.getWordDict().get("test").getName(), "test")
        self.assertTrue(doc.hasWord("test"))

    def test_docWords(self):
        docWords = DocQueue(3)
        doc1 = Document("hello my hello name is what what")
        doc2 = Document("test test nice nice okay")
        TfIdf1 = docWords.calcTfIdf("hello", "happy", doc1)
        docWords.addDoc(doc1)
        self.assertEqual(len(docWords.getDocQueue()), 1)
        TfIdf2 = docWords.calcTfIdf("nice", "happy", doc2)
        docWords.addDoc(doc2)
        self.assertEqual(len(docWords.getDocQueue()), 2)
        TfIdf3 = docWords.calcTfIdf("nice", "happy", doc2)
        self.assertEqual(len(docWords.getDocQueue()), 2)
        for doc in docWords.getDocQueue():
            print 'doc: {}'.format(doc.getDocString())
            for k, v in doc.getWordDict().iteritems():
                print 'worddict: {} {}'.format(k, v.getWeight())

if __name__ == '__main__':
    unittest.main()
