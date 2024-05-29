# W3Schools, Python Tuples, Update Tuples
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x, type(x))
print(y, type(y))
