#!/usr/bin/env python
# encoding: utf-8
"""
utilities.py

"""
import random
import time
import datetime
import threading
import sys, os
import twitteroauth


class Utility(object):

    @staticmethod
    def currentTimeMillis():
        return int(round(time.time() * 1000));

    @staticmethod
    def currentTimeSeconds():
        return int(round(time.time()))
        
    """
    Gets an authenticated API for MuchMoodyTweet app
    """
    def getAuthenticatedApi():
        # get settings from the settings.py file
        apiKey = API_KEY
        accessToken = ACCESS_TOKEN
        accessSecret = ACCESS_SECRET
        apiSecret = API_SECRET
 
        api = twitter.Api(consumer_key=apiKey,
                          consumer_secret=apiSecret,
                          access_token_key=accessToken,
                          access_token_secret=accessSecret)
        return api
        

