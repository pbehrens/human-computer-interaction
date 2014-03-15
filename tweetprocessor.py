
class TweetProcessor(object):
    "Class for dealing with tweets retrieve from the API"
    
    def __init__(self):
        # Master sums
        self.counts = {'happy': 0, 'angry': 0, 'sad': 0, 'profane': 0, 'happyEm': 0, 'angryEm': 0, 'sadEm': 0}
        
    #def readTweetLogs(self, log):
        #TODO

    def processTweet(self, tweet):
        self.counts['happy'] += tweet.happyWordCount
        self.counts['angry'] += tweet.angryWordCount
        self.counts['sad'] += tweet.sadWordCount
        self.counts['profane'] += tweet.profaneWordCount
        self.counts['happyEm'] += tweet.happyEmoticonCount
        self.counts['angryEm'] += tweet.angryEmoticonCount
        self.counts['sadEm'] += tweet.sadEmoticonCount

    def calcHighest(self):
        highest = max(self.counts.iterkeys(), key=(lambda key: self.counts[key]))
        return highest
