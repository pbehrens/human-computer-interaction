

class Document(object):
    """An object that stores a long string of Tweets to form a document. Also contains a dicitonary of words that have been found within the document with a count"""
    def __init__(self, docString):
        self.doc = docString
        self.wordDict = dict()
    
    def getDocString(self):
        return self.doc

    def setDocString(self, docString):
        this.doc = docString

    def getWordDict(self):
        return self.wordDict

    def addIncrementWord(self, word, count):
        self.wordDict[word] = self.wordDict.get(word, 0) + count
