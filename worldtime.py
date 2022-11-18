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

        # TODO: 동적으로 시간 표시
        WorldTimeListBuilder.build(self, [
            {
                "name": "서울",
                "time": "2019-01-01 00:00:00"
            }
        ])

class WorldTimeListBuilder():
    def build(self, timelist):
        for i, data in enumerate(timelist):
            tkinter.Label(self, text=data["name"]).grid(
                column=0, row=i, sticky="ew")
            tkinter.Label(self, text=data["time"]).grid(
                column=1, row=i, sticky="ew")