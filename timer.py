import tkinter
import time
from tkinter import messagebox


class TimerPage(tkinter.Tk):
    def __init__(self, parent):
        tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.geometry("300x250")
        self.title("타이머")
        self.hour = tkinter.StringVar(value="00")
        self.minute = tkinter.StringVar(value="00")
        self.second = tkinter.StringVar(value="00")
        
        self.hourEntry = tkinter.Entry(self, width=5, font=(
            "Arial", 18, ""), textvariable=self.hour)
        self.hourEntry.place(x=80, y=20)

        self.minuteEntry = tkinter.Entry(self, width=5, font=(
            "Arial", 18, ""), textvariable=self.minute)
        self.minuteEntry.place(x=130, y=20)

        self.secondEntry = tkinter.Entry(self, width=5, font=(
            "Arial", 18, ""), textvariable=self.second)
        self.secondEntry.place(x=180, y=20)

        btn = tkinter.Button(self, text="시작", width=10,
                             bd='5', command=self.submit)
        btn.place(x=180, y=120)
        btn = tkinter.Button(self, text="정지", width=10,
                             bd='5', command=self.submit2)
        btn.place(x=80, y=120)

    def submit(self):
        try:
            temp = int(self.hour.get())*3600 + \
                int(self.minute.get())*60 + int(self.second.get())
        except:
            messagebox.showinfo("타이머", "올바른 값을 입력해주세요")
        while temp > -1:
            mins, secs = divmod(temp, 60)
            hours = 0

            if mins > 60:
                hours, mins = divmod(mins, 60)

            self.hour.set("{0:2d}".format(hours))
            self.minute.set("{0:2d}".format(mins))
            self.second.set("{0:2d}".format(secs))

            self.update()
            time.sleep(1)

            if (temp == 0):
                messagebox.showinfo("타이머", "재시작하시겠습니까?")
            temp -= 1

    def submit2(self):
        time.sleep(15)
        