import tkinter

class MainPage(tkinter.Tk):
    def __init__(self, parent):
        tkinter.Tk.__init__(self, parent)

        self.parent = parent
        self.initialize()

    def initialize(self):
        # set window env
        self.grid()
        self.resizable(False, False)
        self.geometry("300x320+500+140")


app = MainPage(None)
app.title("SCHTime")
app.mainloop()
