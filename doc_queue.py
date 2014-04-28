from document import Document
from word import Word
from collections import deque
import re
import math

PRECISION = 8

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
        for doc in self.docs:
            if(doc.hasWord(word)):
                docsWithWord += 1
        IDF = 0
        if(docsWithWord == 0):
            IDF = 0.0
        else:
            IDF = math.log((len(self.docs) + 1) / float(docsWithWord))
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
