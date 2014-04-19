from document import Document
from word import Word
from collections import deque
import re

PRECISION = 2

class DocWords(object):
    """An object that stores a duque of Documents and list of Words and calculates the TF/IDF"""
    def __init__(self, maxWindow):
        self.docs = deque('', maxWindow)
        self.words = list()

    def getDocQueue(self):
        return self.docs

    def getWordList(self):
        return self.words

    " Adds a word to our real words list "
    def addRealWord(self, word):
        self.words.append(word)

    # Calculates the TF of a word, adds the count of the word to the doc, and stores it in our deque.
    # It then uses the current deque state to calculate IDF, returning the weight.
    # Adds a document to the right side of the deque, pushing off the left if maxWindow is exceeded.
    def calcTfIdf(self, word, document):
        TF = 0.0
        IDF = 0.0
        # Use the document and find each word, counting to calc TF
        docString = document.getDocString()
        allWords = re.split(r'\W', docString)
        allWordCount = len(allWords)
        thisWordCount = allWords.count(word)
        # Store the count in the document
        document.addIncWord(word, thisWordCount)
        # Add the document to our deque
        self.docs.append(document)
        # Calc the TF
        TF = round(thisWordCount / float(allWordCount), PRECISION)
        print 'TF CALC: {} / {} = {}'.format(thisWordCount, allWordCount, TF)
        # Calc the IDF
        docsWithWord = 0
        for doc in self.docs:
            if(doc.hasWord(word)):
                docsWithWord += 1
        IDF = round(len(self.docs) / float(docsWithWord), PRECISION)
        print 'IDF CALC: {} / {} = {}'.format(len(self.docs), docsWithWord, IDF)
        # TODO
        TfIdf = TF * IDF
        realWord = Word(word)
        realWord.setTF(TF)
        realWord.setIDF(IDF)
        self.words.append(realWord)
        return TfIdf
