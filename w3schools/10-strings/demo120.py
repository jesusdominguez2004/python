# W3Schools, Python Strings, String Methods
txt = "Mi casa, su casa."
x = txt.rindex("casa")
print(x)

txt = "Hello, welcome to my world."
x = txt.rindex("e")
print(x)

txt = "Hello, welcome to my world."
x = txt.rindex("e", 5, 10)
print(x)

txt = "Hello, welcome to my world."
print(txt.rfind("q"))
print(txt.rindex("q"))
