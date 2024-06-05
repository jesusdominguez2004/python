# W3Schools, Python Scope
def myfunc():
    global x
    x = 300

myfunc()

print(x)    # outputs 300
