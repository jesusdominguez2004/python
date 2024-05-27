# Python Turtle, Sierpinski Curve
import math
import turtle

def one_side(ttl: turtle.Turtle, s, diag, level):
    if level == 0:
        return
    else:
        one_side(ttl, s, diag, level - 1)
        ttl.right(45)
        ttl.forward(diag)
        ttl.right(45)
        one_side(ttl, s, diag, level - 1)
        ttl.left(90)
        ttl.forward(s)
        ttl.left(90)
        one_side(ttl, s, diag, level - 1)
        ttl.right(45)
        ttl.forward(diag)
        ttl.right(45)
        one_side(ttl, s, diag, level - 1)

def sierpinski(ttl: turtle.Turtle, s, level):
    diag = s / math.sqrt(2)
    for i in range(4):
        one_side(ttl, s, diag, level)
        ttl.right(45)
        ttl.forward(diag)
        ttl.right(45)

bob = turtle.Turtle()
bob.speed(0)
bob.pensize(2)
sierpinski(bob, 10, 3)
turtle.done()
