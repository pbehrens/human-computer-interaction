#!/usr/bin/env python
# encoding: utf-8

"""
gui.py

A simple GUI that can display colors
"""

import Tkinter as tk

class Gui(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master.title('Much Twitter')
        self.color = 'white'
        #TODO do we need grid? self.grid(column=0, row=0, ipadx=100, ipady=100, sticky=('N','W','E','S'))
        self.configure(background=self.color)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.pack(fill="both", expand=True, ipadx=100, ipady=100)
        self.createWidgets()
        
    def createWidgets(self):
        self.quitButton = tk.Button(self, text='Quit', command=self.quit)
        self.quitButton.grid()

    def stopGui(self):
        self.quit

    def setColor(self, color):
        self.color = color
        self.configure(background=self.color)

""" Example execution """
#app = Gui()
#app.mainloop()      
