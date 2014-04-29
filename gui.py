#!/usr/bin/env python
# encoding: utf-8

"""
gui.py

A simple GUI that can display colors
"""

import Tkinter as tk
import sys
# from main import searchEvent

searchText = "hello"

class Gui(tk.Frame):
    def __init__(self, quitCallback, get_string, master=None):
        tk.Frame.__init__(self, master)
        self.master.title('Much Twitter')
        self.quitCallback = quitCallback
        self.get_string = get_string
        self.color = 'white'
        #TODO do we need grid? self.grid(column=0, row=0, ipadx=100, ipady=100, sticky=('N','W','E','S'))
        self.configure(background=self.color)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.pack(fill="both", expand=True, ipadx=100, ipady=100)
        self.createWidgets()


    def stopGui(self):
        self.destroy()
        sys.exit(0)

    def createWidgets(self):
        #TODO text box for search query text

        self.search = tk.Entry(self)
        self.search.grid()

        self.submit_button = tk.Button(self, text="Submit", command=self.get_string)
        self.submit_button.grid()

        b = self.quitButton = tk.Button(self, text='Quit', command=self.quitCallback)
        self.quitButton.grid()

    def setColor(self, color):
        self.color = color
        self.configure(background=self.color)



""" Example execution """
#app = Gui()
#app.mainloop()      
