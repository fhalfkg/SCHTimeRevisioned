import tkinter
from tkinter.font import Font
from time import sleep
from threading import Thread


class StopwatchPage(tkinter.Tk):
    def __init__(self, parent):
        tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()
        self.thread.start()

    def initialize(self):
        self.minsize(385, 100)
        self.geometry("600x185+800+140")
        self.title("스톱워치")
        self.saved = []
        self.seconds = 0
        self.minutes = 0
        self.hours = 0
        self.time = "00:00:00"
        self.active = False
        self.kill = False
        self.left = tkinter.Frame(self)
        self.clock = tkinter.Label(
            self.left, text=str(self.time), font=Font(size=36))
        self.button_frame = tkinter.Frame(self.left)
        self.active_button = tkinter.Button(
            self.button_frame, text="시작", command=self.start)

        self.left.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=1)
        self.clock.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
        self.button_frame.pack(side=tkinter.BOTTOM,
                               fill=tkinter.BOTH, expand=1)
        self.active_button.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=1)

        self.thread = Thread(target=self.update, daemon=True)

    def update(self):
        while True:
            if self.kill:
                break
            if self.active:
                if self.seconds < 59:
                    self.seconds += 1
                elif self.seconds == 59:
                    self.seconds = 0
                    self.minutes += 1
                    if self.minutes == 60:
                        self.minutes = 0
                        self.hours += 1
                if self.minutes == 60:
                    self.minutes == 0
                    self.hours += 1
                if len(str(self.seconds)) == 1:
                    self.seconds = "0" + str(self.seconds)
                if len(str(self.minutes)) == 1:
                    self.minutes = "0" + str(self.minutes)
                if len(str(self.hours)) == 1:
                    self.hours = "0" + str(self.hours)
                self.time = f"{self.hours}:{self.minutes}:{self.seconds}"
                self.clock["text"] = self.time
                if isinstance(self.seconds, str):
                    self.seconds = int(self.seconds)
                if isinstance(self.minutes, str):
                    self.minutes = int(self.minutes)
                if isinstance(self.hours, str):
                    self.hours = int(self.hours)
                sleep(1)

    def start(self):
        self.active = True
 