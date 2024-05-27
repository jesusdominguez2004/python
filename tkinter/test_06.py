# Python Tkinter, Test 06:

# Importar librería:
import tkinter

# Definir ventana:
miVentana = tkinter.Tk()

# Propiedades ventana:
miVentana.geometry("300x300")

# Elementos ventana:
miBoton1 = tkinter.Button(miVentana, text = "Botón 1", width = 10, height = 2)
miBoton2 = tkinter.Button(miVentana, text = "Botón 2", width = 10, height = 2)
miBoton3 = tkinter.Button(miVentana, text = "Botón 3", width = 10, height = 2)
miBoton4 = tkinter.Button(miVentana, text = "Botón 4", width = 10, height = 2)
miBoton5 = tkinter.Button(miVentana, text = "Botón 5", width = 10, height = 2)
miBoton6 = tkinter.Button(miVentana, text = "Botón 6", width = 10, height = 2)
miBoton7 = tkinter.Button(miVentana, text = "Botón 7", width = 10, height = 2)
miBoton8 = tkinter.Button(miVentana, text = "Botón 8", width = 10, height = 2)
miBoton9 = tkinter.Button(miVentana, text = "Botón 9", width = 10, height = 2)

miBoton1.grid(row = "0", column = "0")
miBoton2.grid(row = "0", column = "1")
miBoton3.grid(row = "0", column = "2")
miBoton4.grid(row = "1", column = "0")
miBoton5.grid(row = "1", column = "1")
miBoton6.grid(row = "1", column = "2")
miBoton7.grid(row = "2", column = "0")
miBoton8.grid(row = "2", column = "1")
miBoton9.grid(row = "2", column = "2")

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
# font = "fuente tamaño"
# width = "tamaño"
# height = "tamaño"

# elemento["propiedad"] = valor

# Colocar elemento + Ocupar eje:
# miElemento.pack(fill = tkinter.X)
# miElemento.pack(fill = tkinter.Y, expand = True)
# miElemento.pack(fill = tkinter.BOTH, expand = True)

# Colocar elemento + Posición:
# miElemento.pack(side = tkinter.TOP)
# miElemento.pack(side = tkinter.LEFT)
# miElemento.pack(side = tkinter.BOTTOM)
# miElemento.pack(side = tkinter.RIGHT)

# Colocar elemento + Posición tipo tabla
# miElemento.grid(row = "posición", column = "posición")
