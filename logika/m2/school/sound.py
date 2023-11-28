from tkinter import *
from playsound import playsound*
root = Tk()
root.title("Piano")
canvas = Canvas(root, width=670, height=230)
canvas.pack()

class PianoKey:
    