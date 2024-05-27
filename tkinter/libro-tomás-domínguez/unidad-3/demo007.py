# Unidad 3: Posicionamiento y diseño

"""
El gestor de geometría grid() se utiliza para ventanas
complejas, utiliza una construcción de tablas, con filas
y columnas

widtget.grid(opciones):
    column     -> columna del widget, por defecto es la 0
    columnspan -> número de columnas que ocupa el widget, por defecto una
    row        -> fila del widget, por defecto es la 0
    rowspan    -> número de filas que ocupa el widget, por defecto una
    
    ipadx -> pixeles horizontales dentro de sus bordes
    ipady -> pixeles verticales dentro de sus bordes
    padx  -> pixeles horizontales fuera de sus bordes
    pady  -> pixeles verticales fuera de sus bordes

    sticky -> determina la ubicación del widget dentro de una celda cardinalmeente
              NE, SE, SW, NW para ubicar en las esquinas
              N, E, S, W para ubicar en los centros de cada lado

              EW para ocupar todo el ancho de la celda
              NS para ocupar toto el alto de la celda
              NSEW para ocupar toda la celda en ancho y alto

root.columnconfigure(columna, opción, ...)
root.rowconfigure(fila, opción, ...)
    Métodos para configurar aspecto del tamaño de una columna o fila
    concreta empleado diferentes opciones:

    minsize -> tamaño mínmo de la columna o fila especificada en pixeles
    weight -> permite que el tamaño de una columna o fila se adapten al de la ventana principal o widget contenedor
    
    root.columnconfigure(0, weight = 4)
    root.columnconfigure(1, weight = 1)

    root.rowconfigure(0, weight = 4)
    root.rowconfigure(1, weight = 1)

widtget.grid_forget() -> Dejar de mostrar un widget de la ventana principal o frame
"""
from tkinter import Tk, Label
from turtle import bgcolor

filas = 3
columnas = 4

root = Tk()
root.title("demo007")

for fila in range(filas):
    root.rowconfigure(fila, weight=1)
    for columna in range(columnas):
        etiqueta = Label(text="Etiqueta" + str(fila) + str(columna), bg="yellow")
        etiqueta.grid(row=fila, column=columna, padx=2, pady=2)
        root.columnconfigure(columna, weight=1)

root.mainloop()
