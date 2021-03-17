from itertools import cycle
import tkinter as tk


class App(tk.Tk):
    # 
    def __init__(self, image_files, x,y, delay):
        tk.Tk.__init__(self)
        self.geometry('+{}+{}'.format(x,y))
        self.delay = delay
        self.pictures = cycle((tk.PhotoImage(file=image), image) 
        for image in image_files)
        self.pictures_display = tk.Label(self)
        self.pictures_display.pack()
    
    def show_slides(self):
        img_object, img_name = next(self.pictures)
        self.pictures_display.config(image = img_object)
        self.title(img_name)
        self.afte(self.delay,self.show_slides)

    def run(self):
        self.mainloop()
        
delay = 3500

# Image gotten from unsplash.com
image_files = [
    '1.jpg',
    '2.jpg',
    '3.jpg',
    '4.jpg',
    '5.jpg',
    '6.jpg',
    '7.jpg', ]

x = 100
y = 50

imgApp = App(image_files,x,y,delay)
imgApp.show_slides()
imgApp.run()