# W3Schools, Python Operators

# Python Identity Operators
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)       # returns True
print(x is y)       # returns False
print(x == y)       # returns True

print(x is not z)   # returns False
print(x is not y)   # returns True
print(x != y)       # returns False
