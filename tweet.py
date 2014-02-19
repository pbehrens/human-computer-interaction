from moodywords import *
from worddictionary import WordDictionary
class Tweet(object):
    "An object to hold some info about a tweet. Like if it is happy :) or if it is sad :( or if it is neither :|"
    
    def __init__(self, text):
        self.happyWordCount = 0
        self.angryWordCount = 0
        self.sadWordCount = 0
        self.profaneWordCount = 0
        self.happyEmoticonCount = 0
        self.angryEmoticonCount = 0 
        self.sadEmoticonCount = 0
        self.tweet = text
        self.dictionary = WordDictionary()
    
    
    def readTweet(self):
        self.checkEmoticons()
        self.checkWords()
        self.printOut()
        
    def checkWords(self):
        
        for word in self.dictionary.happyWords:
            if word in self.tweet: 
               self.happyWordCount += 1
        for word in self.dictionary.sadWords:
            if word in self.tweet: 
               self.sadWordCount += 1
        for word in self.dictionary.angryWords:
            if word in self.tweet: 
               self.angryWordCount += 1
        for word in self.dictionary.profaneWords:
            if word in self.tweet: 
               self.profaneWordCount += 1
               
    def checkEmoticons(self):
        print ""
               

    def printOut(self):
        print self.tweet
        print "Happy words  " + str(self.happyWordCount)
        print "angry words " + str(self.angryWordCount)
        print "sad words " + str(self.sadWordCount)
        print "profane words " + str(self.profaneWordCount)
        
        
        


        
        
