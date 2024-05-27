# Python Turtle, Circle 02
import turtle

def drawSomeCircles(ttl:turtle):
    ttl.speed(1)
    ttl.pensize(4)
    ttl.penup()
    ttl.home()
    ttl.pendown()
    ttl.pencolor('Green')
    ttl.circle(25)
    ttl.penup()
    ttl.goto(0, 0)
    ttl.pencolor('Red')
    ttl.pendown()
    ttl.circle(50, 180)
    ttl.penup()
    ttl.goto(0, 0)
    ttl.pencolor('Blue')
    ttl.pendown()
    ttl.circle(75, 360, 8)
    ttl.penup()

bob = turtle.Turtle()
drawSomeCircles(bob)

turtle.done()
