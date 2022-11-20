import tkinter
from datetime import datetime
import pytz


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
        self.geometry("300x90+800+200")
        self.title("세계시간")

        self.seoul_label = tkinter.Label(self, text="서울")
        self.seoul_label.grid(column=0, row=0)
        self.seoul_time = tkinter.Label(self, text="00:00:00")
        self.seoul_time.grid(column=1, row=0)

        self.washington_label = tkinter.Label(self, text="워싱턴")
        self.washington_label.grid(column=0, row=1)
        self.washington_time = tkinter.Label(self, text="00:00:00")
        self.washington_time.grid(column=1, row=1)

        self.london_label = tkinter.Label(self, text="런던")
        self.london_label.grid(column=0, row=2)
        self.london_time = tkinter.Label(self, text="00:00:00")
        self.london_time.grid(column=1, row=2)
