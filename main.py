import twitteroauth
from logger import Logger
from tweet import Tweet
from tweetprocessor import TweetProcessor
from gui import Gui
from multiprocessing import Process
import time
from threading import Timer
from threading import Thread

logger = Logger()
api = twitteroauth.getAuthenticatedApi()
tweetprocessor = TweetProcessor()
gui = None
thread = None
timer = None

def searchEvent():
    results = api.GetSearch("Chicago", lang="en")

    for result in results:
        logger.logTweet(result)
        tweet = Tweet(result.text)
        tweet.readTweet()
        tweetprocessor.processTweet(tweet)

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
    timer.start()

def startAppThread():
    thread = Thread(target = searchEvent())
    thread.start()
    thread.join()

def quitCallback():
    print "quitCallback"
    timer.cancel()
    gui.stopGui()
    if(thread != None):
        thread.exit()

if __name__ == '__main__':

    timer = Timer(15, searchEvent)
    gui = Gui(quitCallback)
    _job = gui.after(15000, startAppThread)
    gui.mainloop()
