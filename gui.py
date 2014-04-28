#!/usr/bin/env python
# encoding: utf-8

"""
gui.py

A simple GUI that can display colors
"""

import Tkinter as tk
import sys
# from main import searchEvent


class Gui(tk.Frame):
    def __init__(self, quitCallback, master=None):
        tk.Frame.__init__(self, master)
        self.master.title('Much Twitter')
        self.quitCallback = quitCallback
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
        # frame.pack()
        self.textBox = tk.Text(self, height=1, width=20)
        self.textBox.grid()
        self.enterButton = tk.Button(self, text='Enter', command=self.quitCallback)
        self.enterButton.grid()
        b = self.quitButton = tk.Button(self, text='Quit', command=self.quitCallback)
        self.quitButton.grid()

    def setColor(self, color):
        self.color = color
        self.configure(background=self.color)

    def getString(self):
        return self.textBox.get("0.0",'END-1c')

""" Example execution """
#app = Gui()
#app.mainloop()      
