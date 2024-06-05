# W3Schools, Python Scope
x = 300

def myfunc():
    x = 200
    print(x)

myfunc()    # outputs 200

print(x)    # outputs 300
