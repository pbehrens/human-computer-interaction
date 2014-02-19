from moodywords import *

class Tweet(self):
    "An object to hold some info about a tweet. Like if it is happy :) or if it is sad :( or if it is neither :|"
    
    def __init__(self):
        self.happyWordCount = 0
        self.angryWordCount = 0
        self.sadWordCount = 0
        self.happyEmoticonCount = 0
        self.angryEmoticonCount = 0 
        self.sadEmoticonCount = 0
        self.tweet = ""
        
    
    
    def readTweet(self, tweet):
        self.tweet = tweet
        checkEmoticons(tweet)
        checkWords(tweet)
        printOut()
        
    def checkWords(self, tweet):
        
        for word in HAPPY_WORDS:
            if word in tweet: 
               self.happyWordCount += 1
        for word in SAD_WORDS:
            if word in tweet: 
               self.sadWordCount += 1
        for word in ANGRY_WORDS:
            if word in tweet: 
               self.angryWordCount += 1
               
    def printOut(self, tweet):
        print "Happy words  " + self.happyWordCount
        print "angry words " + self.angryWordCount
        print "sad words " + self.sadWordCount
        
        
        


        
        
