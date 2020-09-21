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
        self.id = canvas.create_oval(10,10,30,30, fill=color)
        self.canvas.move(self.id, 245, 100)
    
    def draw(self):
        pass