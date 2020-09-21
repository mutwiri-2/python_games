from tkinter import *
import time, random

tk = Tk()
tk.title("Bounce")
tk.resizable(0,0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=500, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

# ball class
class Ball():
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.x = 0
        self.y = -1
        self.canvas_height = self.canvas.winfo_height()
        self.id = canvas.create_oval(10,10,30,30, fill=color)
        self.canvas.move(self.id, 245, 100)
    
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 1
        if pos[3] >= self.canvas_height:
            self.y = -1

ball = Ball(canvas, "blue")

# main program loop
while True:
    ball.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)