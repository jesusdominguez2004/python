# Python Turtle, Fractal Triangles
import turtle

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

ken = turtle.Turtle()
ken.color("blue")
ken.speed(0)
draw_outward_triangles(ken, 200)
turtle.mainloop()
