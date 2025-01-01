# Super Script for Turtle Graphics

# needed libraries
import turtle
import colorsys
import math

# SuperScript class
class SuperScript:
    # constructor
    def __init__(self):
        self.turtle = turtle

    # draw a flower
    def draw_flower(self):
        self.turtle.speed(0)
        self.turtle.bgcolor("black")

        h = 0
        for i in range(16):
            for j in range(18):
                c = colorsys.hsv_to_rgb(h, 0.9, 1)
                self.turtle.color(c)
                h = h + 0.005
                self.turtle.rt(90)
                self.turtle.circle(150 - j * 6, 90)
                self.turtle.lt(90)
                self.turtle.circle(150 - j * 6, 90)
                self.turtle.rt(180)
            self.turtle.circle(40, 24)

        self.turtle.done()

    # draw fractal triangles
    def draw_fractal_triangles(self):
        ken = self.turtle.Turtle()
        ken.color("blue")
        ken.speed(0)

        def draw_outward_triangles(ttl: turtle.Turtle, size):
            if size < 10:
                return
            for i in range(3):
                ttl.forward(size / 2)
                insert(ttl, size)
                ttl.forward(size / 2)
                ttl.right(120)

        def insert(ttl: turtle.Turtle, size):
            ttl.left(120)
            draw_outward_triangles(ttl, size / 2)
            ttl.right(120)

        draw_outward_triangles(ken, 200)
        self.turtle.mainloop()

    # draw a heart
    def draw_heart(self):
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
        self.turtle.done()

    # draw a nautilus
    def draw_nautilus(self):
        max = self.turtle.Turtle()

        max.speed(100)
        max.pencolor("cyan")

        self.turtle.bgcolor("black")

        for x in range(240):
            max.circle(x)
            max.left(5)

        self.turtle.mainloop()

    # draw a sierpinski curve
    def draw_sierpinski_curve(self):
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

        bob = self.turtle.Turtle()
        bob.speed(0)
        bob.pensize(2)
        sierpinski(bob, 10, 3)
        self.turtle.done()

    # draw a square
    def draw_square(self, x, y, length):
        bob = self.turtle.Turtle()
        bob.speed(1)
        bob.pensize(3)

        bob.penup()
        bob.goto(x, y)
        bob.setheading(0)
        bob.pendown()
        for _ in range(4):
            bob.forward(length)
            bob.right(90)
        bob.penup()

        self.turtle.done()

    # draw a chessboard
    def draw_chessboard(self, x, y, squaresize):
        matt = turtle.Turtle()
        matt.speed(0)

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
        
        fill = True
        for j in range(8):
            for i in range(8):
                x1 = x + i * squaresize
                y1 = y + j * squaresize
                fill_square(matt, x1, y1, squaresize, fill, 'teal')
                fill = not fill
            fill = not fill

    # draw a circle 01
    def draw_circle_01(self, r, x, y):
        self.turtle.speed(1)
        self.turtle.pensize(3)
        self.turtle.penup()
        angle = self.turtle.heading()
        self.turtle.setheading(0)
        self.turtle.goto(x, y - r)
        self.turtle.pendown()
        self.turtle.circle(r)
        self.turtle.penup()
        self.turtle.setheading(angle)
        self.turtle.done()

    # draw a circle 02
    def draw_circle_02(self):
        self.turtle.speed(1)
        self.turtle.pensize(4)
        self.turtle.penup()
        self.turtle.home()
        self.turtle.pendown()
        self.turtle.pencolor('Green')
        self.turtle.circle(25)
        self.turtle.penup()
        self.turtle.goto(0, 0)
        self.turtle.pencolor('Red')
        self.turtle.pendown()
        self.turtle.circle(50, 180)
        self.turtle.penup()
        self.turtle.goto(0, 0)
        self.turtle.pencolor('Blue')
        self.turtle.pendown()
        self.turtle.circle(75, 360, 8)
        self.turtle.penup()
        self.turtle.done()

    # draw a circle 03
    def draw_circle_03(self):
        ben = self.turtle.Turtle()
        ben.speed(0.5)
        ben.pensize(2)
        ben.penup()
        ben.goto(0, 150)
        ben.pendown()
        ben.pencolor('blue')

        def tanget_circles(tortuga: turtle.Turtle):
            r = 10
            n = 10
            for i in range(1, n + 1, 1):
                tortuga.circle(r * i)

        tanget_circles(ben)

        ben.penup()
        ben.goto(0, -150)
        ben.pendown()
        ben.pencolor('red')

        def concentric_circles(tortuga: turtle.Turtle):
            r = 10
            for i in range(10):
                tortuga.circle(r * i)
                tortuga.penup()
                tortuga.sety((r * i) * (-1))
                tortuga.pendown()

        concentric_circles(ben)

        self.turtle.mainloop()

        
# main driver
if __name__ == '__main__':
    t1 = SuperScript()
    # t1.draw_flower()
    # t1.draw_fractal_triangles()
    # t1.draw_heart()
    # t1.draw_nautilus()
    # t1.draw_sierpinski_curve()
    # t1.draw_square(0, 0, 100)
    # t1.draw_chessboard(0, 0, 20)
    # t1.draw_circle_01(100, 0, 0)
    # t1.draw_circle_02()
    # t1.draw_circle_03()
