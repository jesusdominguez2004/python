# 1) Importar módulo:
import turtle

# 2) Crear el lienzo :
mi_lienzo = turtle.Pen()

# 3) Comandos de movimientos:

# - - Hacia adelante y atrás - -

turtle.forward(50) # Mover hacia adelante (cabeza tortuga)
turtle.forward(-100) # Mover hacia adelante (cabeza tortuga)
turtle.fd(50) # Mover hacia adelante (cabeza tortuga)
turtle.fd(-100) # Mover hacia adelante (cabeza tortuga)

turtle.backward(50) # Mover hacia atrás (cabeza tortuga)
turtle.backward(-100) # Mover hacia atrás (cabeza tortuga)
turtle.bk(50) # Mover hacia atrás (cabeza tortuga)
turtle.bk(-100) # Mover hacia atrás (cabeza tortuga)
turtle.back(50) # Mover hacia atrás (cabeza tortuga)
turtle.back(-100) # Mover hacia atrás (cabeza tortuga)

# - - Girar hacia la derecha o izquierda - -

turtle.right(90) # Girar tortuga hacia la derecha (ángulo)
turtle.rt(90) # Girar tortuga hacia la derecha (ángulo)

turtle.left(90) # Girar tortuga hacia la derecha (ángulo)
turtle.lt(90) # Girar tortuga hacia la derecha (ángulo)

# - - Ir y volver hacia un punto - -

posicion_original = turtle.pos() # Por defecto (0.00, 0.00)

turtle.goto(80,30) # Ir hacia un punto (x,y)
turtle.goto(posicion_original) # Volver hacia un punto (variable)
turtle.setpos(-80,30) # Ir hacia un punto (x,y)
turtle.setpos(posicion_original) # Volver hacia un punto (variable)
turtle.setposition(-80,-30) # Ir hacia un punto (x,y)
turtle.setposition(posicion_original) # Volver hacia un punto (variable)

# - - Ir a coordenada x o coordenada y - -

posicion_original = turtle.pos() # Por defecto (0.00, 0.00)

turtle.setx(80) # Ir coordenada eje x (x, 0.00)
turtle.goto(posicion_original) # Volver hacia un punto (variable)

turtle.sety(80) # Ir coordenada eje y (0.00, y)
turtle.goto(posicion_original) # Volver hacia un punto (variable)

# - - Orientación ángulo tortuga  - -

turtle.setheading(0) # Orientación tortuga (ángulo) ESTE
turtle.setheading(90) # Orientación tortuga (ángulo) NORTE
turtle.setheading(180) # Orientación tortuga (ángulo) OESTE
turtle.setheading(270) # Orientación tortuga (ángulo) SUR

# - - Orientar tortuga y cabeza hacia orientación inicial  - -

turtle.heading() # 0.0° 
turtle.setheading(90) # Orientación tortuga (ángulo) NORTE
turtle.heading() # 90°
turtle.home() # Hacia orientación inicial
turtle.heading() # 0.0°

# - - Dibujar un círculo  - -

# turtle.circle(radio, medida=opcional, pasos=opcional)}
