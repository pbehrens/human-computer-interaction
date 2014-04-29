from collections import deque
import re
from settings import *

PRECISION = 5

class Document(object):
    """An object that stores a long string of Tweets to form a document. Also contains a dicitonary of words that have been found within the document with a count"""
    def __init__(self, docString):
        self.doc = docString
        self.wordDict = dict()

    def getDocString(self):
        return self.doc

    def setDocString(self, docString):
        self.doc = docString
        
    def getWordDict(self):
        return self.wordDict

    " Adds a word to our word dict list, replacing the old if it exists "
    def addRealWord(self, word):
        self.wordDict[word.name] = word

    def hasWord(self, word):
        return word in self.wordDict



class DocQueue(object):
    """An object that stores a duque of Documents and list of Words and calculates the TF/IDF"""
    def __init__(self, maxWindow):
        self.docs = deque('', maxWindow)

    def getDocQueue(self):
        return self.docs

    " Adds a document to the right side of the deque, pushing off the left if maxWindow is exceeded. "
    def addDoc(self, doc):
        self.docs.append(doc)

    # Calculates the TF of a word, adds the count of the word to the doc, and stores it in our deque.
    # It then uses the current deque state to calculate IDF, returning the weight.
    # Returns the document that should be added
    def calcTfIdf(self, word, emotion, document):
        TF = 0.0
        IDF = 0.0
        # Use the document and find each word, counting to calc TF
        docString = document.getDocString()
        allWords = re.split(r'\W', docString)
        allWordCount = len(allWords)
        thisWordCount = allWords.count(word)
        if(thisWordCount > 0):
            print 'FOUND {} {} words'.format(thisWordCount, emotion)
        # Calc the TF
        TF = round(thisWordCount / float(allWordCount), PRECISION)
        if(thisWordCount > 0):
            print 'TF CALC: {} / {} = {}'.format(thisWordCount, allWordCount, TF)
        # Calc the IDF
        docsWithWord = 0
        if(thisWordCount > 0):
            docsWithWord = 1
        for doc in self.docs:
            if(doc.hasWord(word)):
                docsWithWord += 1
        IDF = 0
        if(docsWithWord == 0):
            IDF = 0.0
        else:
            IDF = round((len(self.docs) + 1) / float(docsWithWord), PRECISION)
        if(thisWordCount > 0):
            print 'IDF CALC: {} / {} = {}'.format(len(self.docs), docsWithWord, IDF)
        # Calc the TfIdf
        TfIdf = round(TF * IDF, PRECISION)
        if(thisWordCount > 0):
            print 'WEIGHT: {}'.format(TfIdf)
        realWord = Word(word)
        realWord.setTF(TF)
        realWord.setIDF(IDF)
        realWord.setWeight(TfIdf)
        realWord.setEmo(emotion)
        document.addRealWord(realWord)
        return document



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
