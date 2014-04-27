from settings import *

class Word(object):
    """An object that takes the place of a TF/IDF word, containing its TF, IDF, name, and calc weight"""
    def __init__(self, name):
        self.name = name
        self.TF = 0.0
        self.IDF = 0.0
        self.Weight = 0.0
        self.emo = ""

    def getName(self):
        return self.name

    def getTF(self):
        return self.TF

    def getIDF(self):
        return self.IDF

    def getWeight(self):
        return self.Weight

    def getEmo(self):
        return self.emo

    def setName(self, name):
        self.name = name

    def setTF(self, TF):
        self.TF = TF

    def setIDF(self, IDF):
        self.IDF = IDF

    def setEmo(self, emo):
        self.emo = emo

    def setWeight(self, weight):
        self.Weight = weight

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

    def getAll(self):
        return self.happyWords + self.sadWords + self.angryWords + self.profaneWords
