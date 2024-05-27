# Python Tkinter, Hola Mundo:

# Importar librería:
from tkinter import Tk, Label

# Crear ventana:
root = Tk()

# Propiedades de la ventanas:
root.title("Mensaje")
root.geometry("250x50")
root.resizable(True, False)
root.minsize(200, 50)
root.maxsize(400, 50)

# Widgets de la ventanas:
etiqueta = Label(text="\n  ¡Hola mundo!  \n")
etiqueta.pack()

# Iniciar ventana principal:
root.mainloop()
