from tkinter import *
from PIL import ImageGrab
 
def getter(widget):
    widget.update()
    x=self.winfo_rootx()+widget.winfo_x()
    y=self.winfo_rooty()+widget.winfo_y()
    x1=x+widget.winfo_width()
    y1=y+widget.winfo_height()
    ImageGrab.grab().crop((x,y,x1,y1)).save("first.jpg")
