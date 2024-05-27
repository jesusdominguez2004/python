# Python Tkinter, Test 03:

# Importar librería:
import tkinter

# Definir ventana:
miVentana = tkinter.Tk()

# Propiedades ventana:
miVentana.geometry("300x300")

# Funciones:
def saludo(nombre):
    print("¡Hola " + nombre)

# Elementos ventana:
miBoton1 = tkinter.Button(miVentana, text="Click aquí", command=lambda: saludo("Jesús!"))
miBoton1.pack()

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
