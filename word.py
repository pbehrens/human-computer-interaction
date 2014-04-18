
class Word(object):
    """An object that takes the place of a TF/IDF word, containing its TF, IDF, name, and calc weight"""
    def __init__(self, name):
        self.name = name
        self.TF = 0.0
        self.IDF = 0.0

    def getName(self):
        return self.name

    def getTF(self):
        return self.TF

    def getIDF(self):
        return self.IDF

    def getWeight(self):
        return (self.TF * self.IDF)

    def setName(self, name):
        self.name = name

    def setTF(self, TF):
        self.TF = TF

    def setIDF(self, IDF):
        self.IDF = IDF
