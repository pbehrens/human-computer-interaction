
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

#    def addIncWord(self, word, count):
#        self.wordDict[word] = self.wordDict.get(word, 0) + count

    " Adds a word to our word dict list, replacing the old if it exists "
    def addRealWord(self, word):
        self.wordDict[word.getName()] = word

    def hasWord(self, word):
        return (word in self.wordDict)
