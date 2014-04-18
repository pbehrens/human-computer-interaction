from moodywords import *
from worddictionary import WordDictionary
from logger import Logger
import sys
import re

class Tweet(object):
    "An object to hold some info about a tweet. Like if it is happy :) or if it is sad :( or if it is neither :|"
    
    def __init__(self, tweet):
        self.tweetObject = tweet
        self.happyWordCount = 0
        self.angryWordCount = 0
        self.sadWordCount = 0
        self.profaneWordCount = 0
        self.happyEmoticonCount = 0
        self.angryEmoticonCount = 0 
        self.sadEmoticonCount = 0
        self.tweet = self.tweetObject
        self.dictionary = WordDictionary()
        self.checked = False
        self.logger = Logger()
    
    
    def readTweet(self):
        #TODO self.checkEmoticons()
        self.checkWords()
        self.printOut()

    def checkWords(self):
        if(self.checked is False):
            self.checked = True
            for word in self.dictionary.happyWords:
                if re.search(r'\b({0})\b'.format(word), self.tweet, flags=re.IGNORECASE):
                   self.happyWordCount += 1
            for word in self.dictionary.sadWords:
                if re.search(r'\b({0})\b'.format(word), self.tweet, flags=re.IGNORECASE):
                   self.sadWordCount += 1
            for word in self.dictionary.angryWords:
                if re.search(r'\b({0})\b'.format(word), self.tweet, flags=re.IGNORECASE):
                   self.angryWordCount += 1
            for word in self.dictionary.profaneWords:
                if re.search(r'\b({0})\b'.format(word), self.tweet, flags=re.IGNORECASE):
                   self.profaneWordCount += 1
               
    def getEmotionArray(self):
        if(self.checked is False):
            self.checkWords
        return {"happywords":self.happyWordCount, "sadwords":self.sadWordCount,
                 "angrywords":self.angryWordCount, "profanewords":self.profaneWordCount }
               
    def recordTweet(self):
        if(self.checked is False):
            self.checkWords
        logger.logTweet(self.tweet)
        logger.logMood(self.getEmotionArray())

    def printOut(self):
    	tweetEncode = self.tweet.encode('utf-8')
        print tweetEncode
        print "Happy words  " + str(self.happyWordCount)
        print "angry words " + str(self.angryWordCount)
        print "sad words " + str(self.sadWordCount)
        print "profane words " + str(self.profaneWordCount)
