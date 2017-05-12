# Imports
from Tkinter import *
from sys import *
import os
import platform
import lib
from lib import *

# Predefining Variables

# OOP Data

class CApplication():
    def __screen(self, event):
        w,h = event.width, event.height
        for config in self.configs:
            config(w,h)
    def __init__(self, width, height, title):
        # Predefining Variables
        self.configs = []

        self.root = Tk()

        # Root Bindings
        self.root.bind("<Configure>", self.__screen)

        # Base Values for different frameworks
        self.baseTitle = title
        self.baseWidth = width
        self.baseHeight = height

        self.root.title(title)

        self.root.geometry(str(self.baseWidth)+"x"+str(self.baseHeight)) # Setting the start window size
    def exe(self):
        self.root.mainloop()

class Menubar():
    def __init__(self, app):
        self.app = app
        self.menu = Menu(app.root)

    def Append(self, menu, lbl):
        self.menu.add_cascade(label=lbl, menu=menu)

    def retch(self):
        app.config(menu=self.menu)
        return app

class SubMenu():
    def __init__(self, menu):
        self.menu = menu
    def Append(self, item, options):
        if options["command"] != None and options["command"] != "":
            self.menu.add_command(label=item, command=options["command"])
        elif options["command"] == None or options["command"] == "":
            self.menu.add_command(label=item)
