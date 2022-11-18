import tkinter

class WorldTimePage(tkinter.Tk):
    def __init__(self, parent):
        tkinter.Tk.__init__(self, parent)

        self.parent = parent
        self.initialize()

        

    def initialize(self):
        # set window env
        self.grid()
        self.grid_columnconfigure((0, 1), weight=1)
        self.resizable(False, False)
        self.geometry("300x320+800+140")
        self.title("세계시간")

