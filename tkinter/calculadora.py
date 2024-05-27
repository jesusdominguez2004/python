# Python Tkinter, Test 07:

# Importar librería con todos sus elementos:
from tkinter import *

# Definir ventana:
miVentana = Tk()
miVentana.title("Ejemplo 7 | Pyhton")

# Variables:
i = 0

# Funciones:
def clickBoton(valor):
    global i # Llamar index
    miCuadroTexto.insert(i, valor) # Insertar valor
    i = i + 1 # Index aumentado

def borrar():
    global i # Llamar index
    miCuadroTexto.delete(0, END) # Borrar todo
    i = 0 # Index reiniciado

def hacerOperacion():
    miEcuacion = miCuadroTexto.get() # Obtener ecuación
    miResultado = eval(miEcuacion) # Transformar y resolver
    miCuadroTexto.delete(0, END) # Borrar todo
    miCuadroTexto.insert(0, miResultado) # Insertar resultado
    i = 0 # Index reiniciado
    
# Elementos ventana:
miCuadroTexto = Entry(miVentana, font = ("Calibri 15"))

miBoton1 = Button(miVentana, text = "1", width = "5", height = "2", command = lambda: clickBoton(1))
miBoton2 = Button(miVentana, text = "2", width = "5", height = "2", command = lambda: clickBoton(2))
miBoton3 = Button(miVentana, text = "3", width = "5", height = "2", command = lambda: clickBoton(3))
miBoton4 = Button(miVentana, text = "4", width = "5", height = "2", command = lambda: clickBoton(4))
miBoton5 = Button(miVentana, text = "5", width = "5", height = "2", command = lambda: clickBoton(5))
miBoton6 = Button(miVentana, text = "6", width = "5", height = "2", command = lambda: clickBoton(6))
miBoton7 = Button(miVentana, text = "7", width = "5", height = "2", command = lambda: clickBoton(7))
miBoton8 = Button(miVentana, text = "8", width = "5", height = "2", command = lambda: clickBoton(8))
miBoton9 = Button(miVentana, text = "9", width = "5", height = "2", command = lambda: clickBoton(9))
miBoton0 = Button(miVentana, text = "0", width = "13", height = "2", command = lambda: clickBoton(0))

miBotonBorrar = Button(miVentana, text = "AC", width = "5", height = "2", command = lambda: borrar())
miBotonParentesis1 = Button(miVentana, text = "(", width = "5", height = "2", command = lambda: clickBoton("("))
miBotonParentesis2 = Button(miVentana, text = ")", width = "5", height = "2", command = lambda: clickBoton(")"))
miBotonPunto = Button(miVentana, text = ".", width = "5", height = "2", command = lambda: clickBoton("."))

miBotonDividir = Button(miVentana, text = "/", width = "5", height = "2", command = lambda: clickBoton("/"))
miBotonMultiplicar = Button(miVentana, text = "x", width = "5", height = "2", command = lambda: clickBoton("*"))
miBotonSumar = Button(miVentana, text = "+", width = "5", height = "2", command = lambda: clickBoton("+"))
miBotonRestar = Button(miVentana, text = "-", width = "5", height = "2", command = lambda: clickBoton("-"))
miBotonIgual = Button(miVentana, text = "=", width = "5", height = "2", command = lambda: hacerOperacion())

# Posicionar elementos ventana:
miCuadroTexto.grid(row = "0", column = "0", columnspan = "4", padx = "5", pady = "5")

miBotonBorrar.grid(row = "1", column = "0", padx ="5", pady = "5")
miBotonParentesis1.grid(row = "1", column = "1", padx ="5", pady = "5")
miBotonParentesis2.grid(row = "1", column = "2", padx ="5", pady = "5")
miBotonDividir.grid(row = "1", column = "3", padx ="5", pady = "5")

miBoton7.grid(row = "2", column = "0", padx ="5", pady = "5")
miBoton8.grid(row = "2", column = "1", padx ="5", pady = "5")
miBoton9.grid(row = "2", column = "2", padx ="5", pady = "5")
miBotonMultiplicar.grid(row = "2", column = "3", padx ="5", pady = "5")

miBoton4.grid(row = "3", column = "0", padx ="5", pady = "5")
miBoton5.grid(row = "3", column = "1", padx ="5", pady = "5")
miBoton6.grid(row = "3", column = "2", padx ="5", pady = "5")
miBotonSumar.grid(row = "3", column = "3", padx ="5", pady = "5")

miBoton1.grid(row = "4", column = "0", padx ="5", pady = "5")
miBoton2.grid(row = "4", column = "1", padx ="5", pady = "5")
miBoton3.grid(row = "4", column = "2", padx ="5", pady = "5")
miBotonRestar.grid(row = "4", column = "3", padx ="5", pady = "5")

miBoton0.grid(row = "5", column = "0", columnspan = "2", padx ="5", pady = "5")
miBotonPunto.grid(row = "5", column = "2", padx ="5", pady = "5")
miBotonIgual.grid(row = "5", column = "3", padx ="5", pady = "5")

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
