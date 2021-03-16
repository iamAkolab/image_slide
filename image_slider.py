from itertools import cycle
import tkinter as tk

class App(tk.Tk):
    def __init__(self, image_files, x,y, delay):
        tk.Tk.__init__(self)
        self.geometry('+ {}+ {}'.format(x,y))
        self.delay = delay
        self.pictures = cycle((tk.PhotoImage(file=image), image) 
        for image in image_files)
        self.pictures_display = tk.Label(self)
        self.pictures_display.pack()

