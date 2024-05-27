# Python Tkinter, Test 05:

# Importar librería:
import tkinter

# Definir ventana:
miVentana = tkinter.Tk()

# Propiedades ventana:
miVentana.geometry("300x150")

# Funciones:
def capturarTexto():
    texto = miCajaTexto.get()
    miEtiqueta["text"] = texto

# Elementos ventana:
miCajaTexto = tkinter.Entry(miVentana, font = "Helvetica 15")
miCajaTexto.pack()

miBoton = tkinter.Button(miVentana, text = "Click aquí", command = capturarTexto)
miBoton.pack()

miEtiqueta = tkinter.Label(miVentana, bg = "blue")
miEtiqueta.pack(fill = tkinter.X, side = tkinter.BOTTOM)

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
