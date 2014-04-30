import twitter
import getpass
import twitteroauth
from settings import *
from document import WordDictionary
from logs import Logger
import sys
import re

class TwitterSearch(object):
    "Class for searching the Twittersphere using the API"
    """
    geocode format  geocode='37.781157,-122.398720,1mi'  lat,lon,radius
    
     GetSearch(self, term=None, geocode=None, since_id=None, max_id=None, 
                 until=None, count=15, lang=None, locale=None, result_type='mixed', include_entities=None)
    """
    
    def __init__(self, twitterApi):
        self.api = twitteroauth.getAuthenticatedApi()
        self.lang = "en"
        self.resultType = "mixed"
        self.geocode = None
    
        
    def setLanguage(self, lang):
        self.language = lang

    def setGeocode(self, lat, lon, radius):
        self.geocode = lat + "," + lon + "," + radius + "mi"
        
        #can be mixed, recent, popular
    def setResultType(self, resultType="mixed"):
        self.resultType = resultType
        
    def searchForText(self, text):
        self.api.GetSearch("CTA", lang="en")
        
    def search(self, text):
        results =  self.api.GetSearch(text, lang=self.lang, result_type=self.resultType,  )
        


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



class TweetProcessor(object):
    "Class for dealing with tweets retrieve from the API"
    
    def __init__(self):
        # Master sums
        self.counts = {'happy': 0.0, 'angry': 0.0, 'sad': 0.0, 'profane': 0.0, 'happyEm': 0.0, 'angryEm': 0.0, 'sadEm': 0.0}
        
    #def readTweetLogs(self, log):
        #TODO

    def processTweet(self, tweet):
        self.counts['happy'] += tweet.happyWordCount
        self.counts['angry'] += tweet.angryWordCount
        self.counts['sad'] += tweet.sadWordCount
        self.counts['profane'] += tweet.profaneWordCount
        self.counts['happyEm'] += tweet.happyEmoticonCount
        self.counts['angryEm'] += tweet.angryEmoticonCount
        self.counts['sadEm'] += tweet.sadEmoticonCount

    def processWeights(self, docWords):#realWordList):
        self.clearCounts()
        for doc in docWords.getDocQueue():
            for w, rWord in doc.getWordDict().iteritems():
                print 'WORD WEIGHT AFTER: {}'.format(rWord.getWeight())
                if(rWord.getEmo() == "happy"):
                    self.counts['happy'] += rWord.getWeight()
                if(rWord.getEmo() == "angry"):
                    self.counts['angry'] += rWord.getWeight()
                if(rWord.getEmo() == "sad"):
                    self.counts['sad'] += rWord.getWeight()
                if(rWord.getEmo() == "profane"):
                    self.counts['profane'] += rWord.getWeight()

    def calcHighest(self):
        highest = max(self.counts.iterkeys(), key=(lambda key: self.counts[key]))
        return highest

    def clearCounts(self):
        self.counts['happy'] = 0.0
        self.counts['angry'] = 0.0
        self.counts['sad'] = 0.0
        self.counts['profane'] = 0.0
        self.counts['happyEm'] = 0.0
        self.counts['angryEm'] = 0.0
        self.counts['sadEm'] = 0.0

