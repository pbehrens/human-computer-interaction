#!/usr/bin/env python
# encoding: utf-8

"""
phlogs.py

Created by Patrick Andre Behrens on 2013-10-15.
Copyright (c) 2013 __RamaLabsLLC__. All rights reserved.
"""
import time
from threading import Thread # This is the right package name
import threading
import ctypes
from utils import Utility
import csv
import codecs
import string
from settings import *

class Logger(object):
    "Class for logging tweet data"
    def __init__(self, messageFileName="messages.csv"):
        self.messageFileName = messageFileName
        self.messageLogger = csv.writer(open( self.messageFileName, 'wb'))

        self.tweetLogger = csv.writer(open(TWEET_LOGS , 'wb'))
        self.tweetReader = csv.reader((open(TWEET_LOGS, 'rb')))
        self.tweetLogs = None
        
        self.moodLogger = csv.writer(open(MOOD_LOGS , 'wb'))
        self.moodReader = csv.reader((open(MOOD_LOGS, 'rb')))
        self.moods = None
        
        self.util = Utility()
        self.time = self.util.currentTimeSeconds()
        
        self.idCounter = 0
        
        
        
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
        
        self.tweetLogger.writerow([self.util.currentTimeSeconds(), tweet.created_at, cleanText, tweet.lang, tweet.location])
    
    def logMood(self, moodArray):
        lastRow = self.getLastRow(MOOD_LOGS)
        rowId = lastRow[0]
        self.lastRowId = rowId
        if(self.idCounter > 30):
            self.idCounter = 0
            self.lastRowId += 1
        
        self.moodCounter += 1
        self.moodLogger.writerow(lastRowId, moodArray['happy'], moodArray['sad'], moodArray['angry'], moodArray['profane'])
    
    def readMoodLogs(self):
        self.moods = []
        
        for row in self.moodReader:
            moods.append(row)
            print(row)
        return moods
        
    def addUpMood(self):
        self.mood = []
        happy = 0
        sad = 0
        angry = 0
        profane = 0
        
        
        currentId = None
        for row in self.moodReader:
            
            if(currentId < row[0]):
                currentId = row[0]
                
                
            happy += row[0]
            sad += row[1]
            angry += row[2]
            profane += row[3]
            
            
            moods.append(row)
            print(row)
            
    def getLastRow(self, fileName):
        with open(fileName,'rb') as f:
            reader = csv.reader(f)
            lastline = reader.next()
            for line in reader:
                lastline = line
            return lastline
        
        
    def readTweetLogs(self):
        self.tweetLogs = []
        
        for row in self.tweetReader:
            print(row)
            print('\n')
            self.tweetLogs.append(row)
        return self.tweetLogs    
        
        
        