from tkinter import*
from  pygame import*
#pip install pygame in console
mixer.init()
root = Tk()
root.title("хзхзхзхзх")
canvas = Canvas(root, width=670, height=230)
canvas.pack()

class Videosprite:
    def __init__(self, x, y, frames):
        self.images = []
        for name in frames:
            self.images.append(PhotoImage(file=name))
        self.id = canvas.create_image(x, y, anchor=NW, image=self.images[0])
        self.cur_frame = 0
        self.animate()

    def animate(self):
        root.update()
        self.cur_frame += 1
        if self.cur_frame >= len(self.images):
            self.cur_frame = 0
        canvas.itemconfig(self.id, image=self.images[self.cur_frame])
        root.after(100, self.animate)

class PianoKey:
    def __init__(self, x, y, color, soundfile):
        self.x = x
        self.y = y
        self.color = color
        self.soundfile = soundfile
        w, h = 50, 200
        if color == "black":
            w, h = 40, 140
        self.id = canvas.create_rectangle(x, y, x+w, y+h, fill=color)
        canvas.tag_bind(self.id, "<1>", self.onclick)

    def onclick(self, e):
        mixer.music.load(self.soundfile)

PianoKey(15, 15, "white", "notes/note do.ogg")
PianoKey(70, 15, "white", "notes/note re.ogg")
PianoKey(125, 15, "white", "notes/note mi.ogg")
PianoKey(180, 15, "white", "notes/note fa.ogg")
PianoKey(235, 15, "white", "notes/note sol.ogg")
PianoKey(290, 15, "white", "notes/note la.ogg")
PianoKey(345, 15, "white", "notes/note si.ogg")
PianoKey(400, 15, "white", "notes/note do2.ogg")

PianoKey(47.5, 15, "black", "notes/note do-d.ogg")
PianoKey(102.5, 15, "black", "notes/note mi-b.ogg")
PianoKey(212.5, 15, "black", "notes/note fa-d.ogg")
PianoKey(267.5, 15, "black", "notes/note sol-d.ogg")
PianoKey(322.5, 15, "black", "notes/note si-d.ogg")

B = Videosprite(460, 15, ["frames/f01.png", "frames/f02.png", "frames/f03.png", "frames/f04.png"])

root.mainloop()


