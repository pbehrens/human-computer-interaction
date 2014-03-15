from settings import *

class WordDictionary(object):
    "Make all the dictionaries available in array form"
    
    def __init__(self):
        self.happyWords = [line.strip() for line in open(DICTIONARY_DIR + '/' + HAPPY_WORDS)]
        self.sadWords = [line.strip() for line in open(DICTIONARY_DIR + '/' + SAD_WORDS)]
        self.angryWords = [line.strip() for line in open(DICTIONARY_DIR + '/' + ANGRY_WORDS)]
        self.profaneWords = [line.strip() for line in open(DICTIONARY_DIR + '/' + PROFANE_WORDS)]
            
    def getHappy(self):
      return self.happyWords
        
    def getSad(self):
        return self.sadWords
    
    def getAngry(self):
        return self.angryWords
        
    def getProfane(self):
        return self.profaneWords
    