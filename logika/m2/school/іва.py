from time import*
from tkinter import*


class Videosprite:
    def __init__(self, x, y, frames):
        self.images = []
        for name in frames:
            self.images.append(PhotoImage(file=name))
        self.id = canvas.create_image(x, y, anchor=NW, image=self.images[0])
        self.cur_frame = 0
        self.animate()
        canvas.tag_bind(self.id, '<1>', self.on_click())

    def animate(self):
        root.update()
        self.cur_frame += 1
        if self.cur_frame >= len(self.images):
            self.cur_frame = 0
        canvas.itemconfig(self.id, image=self.images[self.cur_frame])
        root.after(100, self.animate)

    def on_click(self, e):
        canvas.delete(self.id)


root = Tk()
root.title('Відеоспрайти')
canvas = Canvas(root, width = 140, height = 280)
canvas.pack()
B = Videosprite(5, 5, ['1.gif', '2.gif', '3.gif'])
C = Videosprite(5,140, ['4.gif', '5.gif', '6.gif', '7.gif', '8.gif'])
root.mainloop()
