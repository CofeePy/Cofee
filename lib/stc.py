from Tkinter import *
from Tkinter import Text as textcontrol

class StyledTextControl( textcontrol ):
    def spaces(self, val):
        return str(val*8)
    def __screen(self, width, height):
        self.
    def __init__(self, parent, width, height, fontf, fontsize):
        # Predefining Variables
        self.POS = "RIGHT"

        self.app = parent
        self.widget = textcontrol(parent.mainframe)
        self.widget.config(tabs=self.spaces(4), background="#ffffff", foreground='#000000', highlightthickness=0, borderwidth=0)
        if fontf != None:
            if fontsize != None and fontsize != "":
                self.widget.config(font=(fontf, fontsize))
            else:
                self.widget.config(font=fontf)
    def setMargins(self, top, left, right, ):
    def pack(self):
        self.app.configs.append(self.__screen)
        self.widget.pack(side=self.POS)
