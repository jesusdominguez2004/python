# Python Turtle, Nautilus
import turtle

max = turtle.Turtle()

max.speed(100)
max.pencolor("cyan")

turtle.bgcolor("black")

for x in range(240):
    max.circle(x)
    max.left(5)

turtle.mainloop()
