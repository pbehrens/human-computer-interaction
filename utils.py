#!/usr/bin/env python
# encoding: utf-8
"""
utilities.py

Created by Patrick Andre Behrens on 2014-02-18.
Copyright (c) 2013 . All rights reserved.
"""
import random
import time
import datetime
import threading
import termios, sys, os

class Utility(object):

    @staticmethod
    def currentTimeMillis():
        return int(round(time.time() * 1000));

    @staticmethod
    def currentTimeSeconds():
        return int(round(time.time()))