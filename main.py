import twitteroauth
from logger import Logger
from tweet import Tweet


logger = Logger()
api = twitteroauth.getAuthenticatedApi()


results = api.GetSearch("Chicago", lang="en")


    
for result in results:
    logger.logTweet(result)
    tweet = Tweet(result.text)
    tweet.readTweet()
    
#TODO logger.readTweetLogs()

    
    
    

    
    
