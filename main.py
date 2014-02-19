import twitteroauth
from logger import Logger



logger = Logger()
api = twitteroauth.getAuthenticatedApi()


results = api.GetSearch("CTA", lang="en")


    
for result in results:
    logger.logTweet(result)
    print result.text
    
    
    
    

    
    