# Unidad 3: Posicionamiento y diseño

"""
Tres gestores de geometría de Tkinter:
    pack  -> Organiza los widgets horizontal o verticalmente por defecto de arriba hacia abajo
    grid  -> Distribuye los widgets en cuadícula, como una tabla, recomendado para interfaces complejas
    place -> Coloca los widgets en coordenadas concretas

pack(opciones):
    expand -> Boolean
    fill   -> X, Y, BOTH
    side   -> TOP, BOTTOM, LEFT, RIGHT

    ipadx -> Pixeles horizontales dentro de bordes widgets
    ipady -> Pixeles verticales dentro de bordes widgets
    padx  -> Pixeles horizontales fuera de bordes widgets
    pady  -> Pixeles verticales fuera de bordes widgets

    padx = 10 (Derecha e izquierda)
    padx = (10, 5) (Derecha, izquierda)
    pady = 10 (Derecha e izquierda)
    pady = (10, 5) (Derecha, izquierda)

widtget.pack_forget() -> dejar de mostrar widget en la ventana
"""
from tkinter import Tk, Label, TOP, BOTTOM, LEFT, RIGHT

root = Tk()
root.title("demo005")
root.geometry("200x200")

etiqueta1 = Label(text="Etiqueta1")
etiqueta2 = Label(text="Etiqueta2")
etiqueta3 = Label(text="Etiqueta3")
etiqueta4 = Label(text="Etiqueta4")

etiqueta1.pack(side=TOP, pady=10)
etiqueta2.pack(side=BOTTOM, pady=10)
etiqueta3.pack(side=LEFT, padx=10)
etiqueta4.pack(side=RIGHT, padx=10)

root.mainloop()
