# Python Tkinter, Test 01:

# Importar librería:
import tkinter

# Definir ventana:
miVentana = tkinter.Tk()

# Propiedades ventana:
miVentana.geometry("300x300")

# Elementos ventana:
miEtiqueta = tkinter.Label(miVentana, text="¡Hola mundo!")
miEtiqueta.pack()

# Llamar ventana:
miVentana.mainloop()

# miElemento = tkinter.Tipo(miVentana, propiedades...)
# text = "texto"
# bg = "color"
# padx = "tamaño"
# pady = "tamaño"
# command = nombreFunción SIN ()
# command = lambda: nombreFunción(parámetro)
# command = lambda: print("Hola mundo")

# Colocar elemento + Ocupar eje:
# miElemento.pack(fill = tkinter.X)
# miElemento.pack(fill = tkinter.Y, expand = True)
# miElemento.pack(fill = tkinter.BOTH, expand = True)

# Colocar elemento + Posición:
# miElemento.pack(side = tkinter.TOP)
# miElemento.pack(side = tkinter.LEFT)
# miElemento.pack(side = tkinter.BOTTOM)
# miElemento.pack(side = tkinter.RIGHT)
