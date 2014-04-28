import twitteroauth
from muchtwitter.models.twitter import TweetProcessor
from gui import Gui
from muchtwitter.models.logs import Logger
from muchtwitter.models.document import Document, DocQueue, WordDictionary
import time

QUERY_FREQ = 5000

SEARCH_TERM = "Chicago"
logger = Logger()
api = twitteroauth.getAuthenticatedApi()
tweetprocessor = TweetProcessor()
gui = None
docWords = DocQueue(5)
wordDict = WordDictionary()

def searchEvent():

    # SEARCH_TERM = gui.getString()
    results = api.GetSearch(SEARCH_TERM, lang="en")

    start_time = time.time()
    resultString = ""
    for result in results:
        logger.logTweet(result)
        resultString+= ' ' + result.text
    resultString.lower()
    print resultString
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
    logger.logCounts(tweetprocessor.counts)
    
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

if __name__ == '__main__':
    gui = Gui(quitCallback)
    _job = gui.after(QUERY_FREQ, searchEvent)
    gui.mainloop()
