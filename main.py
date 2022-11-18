import tkinter

class MainPage(tkinter.Tk):
    def __init__(self, parent):
        tkinter.Tk.__init__(self, parent)

        self.parent = parent
        self.initialize()

    def initialize(self):
        # set window env
        self.grid()

app = MainPage(None)
app.mainloop()
