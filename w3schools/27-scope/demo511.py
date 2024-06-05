# W3Schools, Python Scope
def myfunc():
    x = 300
    def myinnerfunc():
        print(x)
    myinnerfunc()

myfunc()    # outputs 300
