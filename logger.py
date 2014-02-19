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

class Logger(object):
    "Class for logging tweet data"
    def __init__(self, logFileName="default"):
        self.logFileName = logFileName
        self.fileHandler = open(self.logFileName, 'w')
        self.fileHandler.write("time,type,message")
        self.fileHandler.close()
        self.util = Utility()
        self.time = self.util.currentTimeSeconds()
        
    def log(self, code, message):
        self.time = self.util.currentTimeMillis()
        print(str(self.time) + "," + str(code) + "," + 
              str(message) + "\n")
        self.fileHandler = open(self.logFileName, 'a')
        self.fileHandler.write(str(self.time) + "," + str(code) + "," + str(message) + "\n")
        self.fileHandler.close()