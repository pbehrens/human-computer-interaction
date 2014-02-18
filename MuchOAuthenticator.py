import twitter
import getpass

apiKey = 'TJF1q00Rpwyn1bN0YOw'
apiSecret = ''
accessToken = '2332779854-KUyrIN82tDfm4DK3MNTaEdY1LcATENmd5GvNGzL'
accessSecret = ''
"""
Gets an authenticated API for MuchMoodyTweet app
"""
def getAuthenticatedApi():
    apiSecret = getpass.getpass('Enter API secret:')
    accessSecret = getpass.getpass('Enter Access Secret:')
    # Remove whitespace
    apiSecret = "".join(apiSecret.split())
    accessSecret = "".join(accessSecret.split())
    accessSecret.replace(" ", "")
    api = twitter.Api(consumer_key=apiKey,
                      consumer_secret=apiSecret,
                      access_token_key=accessToken,
                      access_token_secret=accessSecret)
    return api
