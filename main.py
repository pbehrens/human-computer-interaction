import twitteroauth
from logger import Logger
from tweet import Tweet
from tweetprocessor import TweetProcessor
from gui import Gui
from doc_queue import DocQueue
from document import Document
from worddictionary import WordDictionary
import time

QUERY_FREQ = 5000

# SEARCH_TERM = "Chicago"
logger = Logger()
api = twitteroauth.getAuthenticatedApi()
tweetprocessor = TweetProcessor()
gui = None
docWords = DocQueue(10)
wordDict = WordDictionary()


def searchEvent():

    SEARCH_TERM = get_string()
    print SEARCH_TERM
    if SEARCH_TERM != "":
        results = api.GetSearch(SEARCH_TERM, lang="en")

        start_time = time.time()
        resultString = ""
        for result in results:
            logger.logTweet(result)
            resultString+= ' ' + result.text
        resultString.lower()
        print resultString.encode('utf-8')
        document = Document(resultString)
        # Go through each word list
        for word in wordDict.getHappy():
            tfIdf = docWords.calcTfIdf(word, 'happy', document)
        for word in wordDict.getSad():
            tfIdf = docWords.calcTfIdf(word, 'sad', document)
        for word in wordDict.getAngry():
            tfIdf = docWords.calcTfIdf(word, 'angry', document)
        for word in wordDict.getProfane():
            tfIdf = docWords.calcTfIdf(word, 'profane', document)
        # Add the document to our deque
        docWords.addDoc(document)
        tweetprocessor.processWeights(docWords)#wordList)
        logger.logTiming("tfIdf", (time.time() - start_time), tweetprocessor.calcHighest())

        countAndColor()

def countAndColor():
    highest = tweetprocessor.calcHighest()
    print '\n\n Highest emotion: ' + highest + '\n\n'
    print 'Accumulated so far: '
    print tweetprocessor.counts
    print '\n\n'
    if (highest == 'happy'):
        gui.setColor('green')
    elif (highest == 'angry'):
        gui.setColor('red')
    elif (highest == 'sad'):
        gui.setColor('blue')
    elif (highest == 'profane'):
        gui.setColor('orange')
    # Do process again after 15 sec
    _job = gui.after(QUERY_FREQ, searchEvent)

def quitCallback():
    print "Exited."
    gui.stopGui()

def get_string():
    search_text = gui.search.get()
    return search_text

if __name__ == '__main__':
    gui = Gui(quitCallback,get_string)
    _job = gui.after(QUERY_FREQ, searchEvent)
    gui.mainloop()
