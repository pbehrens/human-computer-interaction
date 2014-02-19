from utils import Utility
from logger import Logger

class OutputController(object):
    "Class for controlling dosage"
    
    def __init__(self):
        self.log = Logger()
        self.colors = []
        self.currentColor = ""
        self.initiateColors()
        
    def initiateColors(self):
        self.colors = ["red", "green", "blue", "orange",  "orangeyellow", "dogwhite", "blizzard", "yellow", "pink", "pinkish"]
        
    def outputColor(self, color):
        if color in self.colors:
            self.color = color
            self.log.log("output", color)
            print(color)
            return self.color
        else:
            self.log.log("output error", color + " could not be printed out")
            return ""
        
        
        
    def getCurrentColor(self):
        self.log.log("check", self.color)
        print("current color is " + self.color)
        return self.color