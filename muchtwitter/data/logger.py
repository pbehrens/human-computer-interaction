#!/usr/bin/env python
# encoding: utf-8


import time
from threading import Thread # This is the right package name
import threading
import ctypes
from utils import Utility
import csv
import codecs
import string

import random
import time
import datetime
import threading
import sys, os



class Logger(object):
    "Class for logging tweet data"
    def __init__(self, messageFileName="default"):
        self.messageFileName = messageFileName
        self.messageLogger = csv.writer(open( self.messageFileName, 'wb'))
        self.messageLogger.writerow(["time", "code", ""])

        self.tweetLogger = csv.writer(open("tweets.csv", 'a'))
    
        self.util = Utility()
        self.time = self.util.currentTimeSeconds()

        self.timeLogger = csv.writer(open("timing.csv", 'wb'))
        self.timeLogger.writerow(['impl', 'execTime', 'highestEmo', 'currentTime'])
        
    def logMessage(self, code, message):
        self.time = self.util.currentTimeMillis()
        self.messageLogger.writerow([self.time, code, message])
        print(str(self.time) + "," + str(code) + "," + 
              str(message) + "\n")
        
    def logTweet(self, tweet):
        self.time = self.util.currentTimeMillis()
        
        # strip out weird chracters preventing the csv to be written
        tweetText = tweet.text
        cleanText = filter(lambda x: x in string.printable, tweetText)
        exclude = set([',', ';'])
        cleanText = ''.join(ch for ch in cleanText if ch not in exclude)
        
        self.tweetLogger.writerow([self.util.currentTimeSeconds(), tweet.created_at, cleanText, tweet.lang, tweet.location])

    def logTiming(self, qualifier, execTime, highestEmo):
        self.time = self.util.currentTimeMillis()
        self.timeLogger.writerow([qualifier, execTime, highestEmo, self.time])
