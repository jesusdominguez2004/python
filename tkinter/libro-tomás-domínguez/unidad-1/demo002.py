# Unidad 1: Introducción

from tkinter import Tk, Label, mainloop

class Interfaz:
    def __init__(self):
        self.etiqueta = Label(text="\n  ¡Hola mundo!  \n")
        self.etiqueta.pack()

root = Tk()
mi_interfaz = Interfaz()

root.mainloop()
#mi_interfaz.etiqueta.mainloop()