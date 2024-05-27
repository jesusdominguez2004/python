# Python Turtle, Circle 01
import turtle

def centeredCircle(ttl:turtle, r, x, y):
    ttl.penup()
    angle = ttl.heading()
    ttl.setheading(0)
    ttl.goto(x, y - r)
    ttl.pendown()
    ttl.circle(r)
    ttl.penup()
    ttl.setheading(angle)

bob = turtle.Turtle()
bob.speed(1)
bob.pensize(3)
centeredCircle(bob, 100, 0, 0)

turtle.done()
