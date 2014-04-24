import twitteroauth
from logger import Logger
from tweet import Tweet
from tweetprocessor import TweetProcessor
from gui import Gui
import time

SEARCH_TERM = 'Chicago'
QUERY_FREQ = 5000

logger = Logger()
api = twitteroauth.getAuthenticatedApi()
tweetprocessor = TweetProcessor()
gui = None
start_time = 0.0

def searchEvent():
    results = api.GetSearch(SEARCH_TERM, lang="en")

    # Log tweets outside of timer
    for result in results:
        logger.logTweet(result)
    start_time = time.time()
    for result in results:
        tweet = Tweet(result.text)
        tweet.readTweet()
        tweetprocessor.processTweet(tweet)
    logger.logTiming("legacy", (time.time() - start_time), tweetprocessor.calcHighest())

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

if __name__ == '__main__':
    gui = Gui(quitCallback)
    _job = gui.after(QUERY_FREQ, searchEvent)
    gui.mainloop()
