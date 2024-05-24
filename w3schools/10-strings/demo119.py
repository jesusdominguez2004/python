# W3Schools, Python Strings, String Methods
txt = "Mi casa, su casa."
x = txt.rfind("casa")
print(x)

txt = "Hello, welcome to my world."
x = txt.rfind("e")
print(x)

txt = "Hello, welcome to my world."
x = txt.rfind("e", 5, 10)
print(x)

txt = "Hello, welcome to my world."
print(txt.rfind("q"))
print(txt.rindex("q"))
