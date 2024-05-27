# Python Turtle, Circle 03
import turtle

def tanget_circles(tortuga: turtle.Turtle):
    r = 10
    n = 10
    for i in range(1, n + 1, 1):
        tortuga.circle(r * i)

def concentric_circles(tortuga: turtle.Turtle):
    r = 10
    for i in range(10):
        tortuga.circle(r * i)
        tortuga.penup()
        tortuga.sety((r * i) * (-1))
        tortuga.pendown()

ben = turtle.Turtle()
ben.speed(0.5)
ben.pensize(2)
ben.penup()
ben.goto(0, 150)
ben.pendown()
ben.pencolor('blue')
tanget_circles(ben)
ben.penup()
ben.goto(0, -150)
ben.pendown()
ben.pencolor('red')
concentric_circles(ben)

turtle.mainloop()
