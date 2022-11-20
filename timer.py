import time
from tkinter import *
from tkinter import messagebox
 
root = Tk()
  
root.geometry("300x250")
  
root.title("Time Counter")
  
hour=StringVar()
minute=StringVar()
second=StringVar()
  
hour.set("00")
minute.set("00")
second.set("00")

hourEntry= Entry(root, width=3, font=("Arial",18,""),
                 textvariable=hour)
hourEntry.place(x=80,y=20)
  
minuteEntry= Entry(root, width=3, font=("Arial",18,""),
                   textvariable=minute)
minuteEntry.place(x=130,y=20)
  
secondEntry= Entry(root, width=3, font=("Arial",18,""),
                   textvariable=second)
secondEntry.place(x=180,y=20)

root.mainloop()