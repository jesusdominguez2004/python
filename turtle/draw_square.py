# Python Turtle, Square
import turtle

def drawSquare(ttl: turtle.Turtle, x, y, length):
    ttl.penup()
    ttl.goto(x, y)
    ttl.setheading(0)
    ttl.pendown()
    for _ in range(4):
        ttl.forward(length)
        ttl.right(90)
    ttl.penup()

bob = turtle.Turtle()
bob.speed(1)
bob.pensize(3)
drawSquare(bob, 0, 0, 100)

turtle.done()
