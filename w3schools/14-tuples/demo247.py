# W3Schools, Python Tuples, Update Tuples
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

print(thistuple, type(thistuple))
print(y, type(y))
