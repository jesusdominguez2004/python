# Python Turtle, Heart
import turtle

heart = turtle.Turtle()
heart.fillcolor('red')
heart.begin_fill()

heart.left(140)
heart.forward(113)

for i in range(200):
    heart.right(1)
    heart.forward(1)

heart.left(120)    

for i in range(200):
    heart.right(1)
    heart.forward(1)

heart.forward(112)
heart.end_fill()
heart.ht()
turtle.done()
