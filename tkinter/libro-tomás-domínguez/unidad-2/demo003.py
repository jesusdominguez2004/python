# Unidad 2: La ventana principal

"""
root.mainloop()
    Iniciar la ventana princial
    es su método principal

root.quit()
    Cierra la ventana principal
    y su método principal

root.title("texto")
    Establece el título de la
    ventana principal
    root.title("Mensaje")
    root.title("Demo3")

root.geometry("anchoxalto") Pixeles
    Establece tamaño por defecto
    de la ventana principal
    root.geometry("200x200")
    root.geometry("300x400")


root.resizable(ancho, alto) Booleanos
    Permite si el usuario modifique 
    el ancho o alto de la ventana
    root.resizable(True, True)
    root.resizable(False, False)
    root.resizable(True, False)
    root.resizable(False, True)

root.minsize(ancho, alto) Pixeles
    Establece las dimensiones mínimas
    de la ventana principal
    root.minsize(200, 200)
    root.minsize(300, 400)

root.maxsize(ancho, alto) Pixeles
    Establece las dimensiones máximas
    de la ventana principal
    root.maxsize(200, 200)
    root.maxsize(300, 400)

root.winfo_height()
    Obtiene el alto de la
    ventana principal

root.winfo_width()
    Obtiene el ancho de la
    ventana principal

root.attributes("-fullscreen", 1)
    Pantalla completa ventana principal

root.withdraw()
    Desaparecer de la pantalla
    ventana principal sin cerrarla,
    pero solo accesible en la barras 
    de tarea de Windows

root.iconify()
    Minimiza ventana principal

root.deiconify()
    Des-Minimiza ventana principal

root.state()
    Conocer estado ventana principal
    
    Valores devueltos:
    "normal" -> la ventana se muestra de forma habitual
    "iconic" -> la ventana se muestra como icono en la barra de tareas
    "withdrawn" -> la ventana ha desaparecido de la pantalla, aunque no se ha cerrado
    "zoomed" -> la ventana ocupa toda la pantalla

    Establecer estado de la ventana y sus equivalencias:
    root.state(newstate="zoomed")
    root.state(newstate="normal") == root.deiconify()
    root.state(newstate="iconic") == root.iconify()
    root.state(newstate="withdrawn") == root.withdraw()

root.destroy()
    Cerrar la ventana principal

root.protocol("WM_DELETE_WINDOW", función)
    Ejecuta una función al recibir el evento
    'cerrar ventana con el ícono superior derecho'

    protocol("evento del sistema", controladorDeProtocolo)
"""

from tkinter import Tk, Label

root = Tk()
root.geometry("250x50")
root.resizable(True, False)
root.minsize(50, 50)
root.maxsize(400, 50)
root.title("demo003")

etiqueta = Label(text="\n  ¡Hola mundo!  \n")
etiqueta.pack()

root.mainloop()
