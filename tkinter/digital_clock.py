# Python Tkinter, Digital Clock:
import tkinter
from time import strftime

top = tkinter.Tk()
top.title("Digital Clock 1")

def none():
    text = strftime(' %H:%M:%S %p')
    lbl.config(text=text)
    lbl.after(1000, none)
    
lbl = tkinter.Label(top, 
    font=("digital-7", 50, "bold"), 
    background="black",
    foreground="green")
lbl.pack(anchor="center")

none()
tkinter.mainloop()
