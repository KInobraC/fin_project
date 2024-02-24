from tkinter import *
from datetime import datetime

def clock():
    now = datetime.now()
    lab.config(text=str(now.hour)+':'+str(now.minute)+':'+str(now.second))
    color = ["red", 'green', 'yellow', 'white', 'grey']
    root.config(bg=color[now.second%5])
    root.after(1000, clock)

root = Tk()
root.geometry('200x100')
root.title("godinik")

lab = Label(root, text="Hello world", font='Arial 18', bg='blue', fg="yellow")
lab.pack(pady=30)

clock()
root.mainloop()
