# W3Schools, Python Tuples, Update Tuples
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

print(thistuple, type(thistuple))
print(y, type(y))
