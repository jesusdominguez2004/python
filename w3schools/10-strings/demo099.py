# W3Schools, Python Strings, String Methods
txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x)

txt = "Hello, welcome to my world."
x = txt.index("e")
print(x)

txt = "Hello, welcome to my world."
x = txt.index("e", 5, 10)
print(x)

txt = "Hello, welcome to my world."
print(txt.find("q"))    # the find() method returns -1
print(txt.index("q"))   # the index() method will raise an exception
print(x)
