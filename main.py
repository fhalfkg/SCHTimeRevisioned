import tkinter
from worldtime import WorldTimePage

class MainPage(tkinter.Tk):
    def __init__(self, parent):
        tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        # set window env
        self.grid()
        self.resizable(False, False)
        self.geometry("300x320+500+200")

        self.WIDTH = 20
        self.HEIGHT = 10


        btn1 = tkinter.Button(self, text="세계시간", width=self.WIDTH,
                              height=self.HEIGHT, command=self.onBtn1Click)
        btn1.grid(column=0, row=0)

        btn2 = tkinter.Button(self, text="스톱워치", width=self.WIDTH,
                              height=self.HEIGHT, command=self.onBtn2Click)
        btn2.grid(column=1, row=0)

        btn3 = tkinter.Button(self, text="타이머", width=self.WIDTH,
                              height=self.HEIGHT, command=self.onBtn3Click)
        btn3.grid(column=0, row=1)

        btn4 = tkinter.Button(self, text="etc", width=self.WIDTH,
                              height=self.HEIGHT, command=self.onBtn4Click)
        btn4.grid(column=1, row=1)

    def onBtn1Click(self):
        WorldTimePage(None).mainloop()

    def onBtn2Click(self):
        pass

    def onBtn3Click(self):
        pass

    def onBtn4Click(self):
        pass


app = MainPage(None)
app.title("SCHTime")
app.mainloop()
