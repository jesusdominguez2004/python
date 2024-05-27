# Python Turtle, Chessboard
import turtle

def draw_square(ttl: turtle.Turtle, x, y, length):
    ttl.penup()
    ttl.goto(x, y)
    ttl.setheading(0)
    ttl.pendown()
    for _ in range(4):
        ttl.forward(length)
        ttl.right(90)
    ttl.penup()

def fill_square(tll: turtle.Turtle, x, y, lenght, fill, color):
    if fill:
        tll.fillcolor(color)
        tll.begin_fill()
        draw_square(tll, x, y, lenght)
        tll.end_fill()
    else:
        draw_square(tll, x, y, lenght)

def draw_chessboard(tll: turtle.Turtle, x, y, squaresize):
    fill = True
    for j in range(8):
        for i in range(8):
            x1 = x + i * squaresize
            y1 = y + j * squaresize
            fill_square(tll, x1, y1, squaresize, fill, 'teal')
            fill = not fill
        fill = not fill

matt = turtle.Turtle()
matt.speed(0)
draw_chessboard(matt, 0, 0, 20)

turtle.mainloop()
