# W3Schools, Python Strings, String Methods
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

# named indexes, numbered indexes, empty placeholders:
txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'm {1}".format("John", 36)
txt3 = "My name is {}, I'm {}".format("John", 36)
print(txt1)
print(txt2)
print(txt3)

# formatting types:
txt = "We have {:<8} chickens."
print(txt.format(49))

txt = "We have {:>8} chickens."
print(txt.format(49))

txt = "We have {:^8} chickens."
print(txt.format(49))

txt = "The temperature is {:=8} degrees celsius."
print(txt.format(-5))

txt = "The temperature is between {:+} and {:+} degrees celsius."
print(txt.format(-3, 7))

txt = "The temperature is between {:-} and {:-} degrees celsius."
print(txt.format(-3, 7))

txt = "The temperature is between {: } and {: } degrees celsius."
print(txt.format(-3, 7))

txt = "The universe is {:,} years old."
print(txt.format(13800000000))

txt = "The universe is {:_} years old."
print(txt.format(13800000000))

txt = "The binary version of {0} is {0:b}"
print(txt.format(5))

# txt = "The unicode version of {0} is {0:c}"
# print(txt.format(5))

txt = "We have {:d} chickens."
print(txt.format(0b101))

txt = "We have {:e} chickens."
print(txt.format(5))

txt = "We have {:E} chickens."
print(txt.format(5))

txt = "The price is {:.2f} dollars."
print(txt.format(45))

txt = "The price is {:f} dollars."
print(txt.format(45))

x = float('inf')
txt = "The price is {:F} dollars."
print(txt.format(x))

x = float('inf')
txt = "The price is {:f} dollars."
print(txt.format(x))

txt = "The octal version of {0} is {0:o}"
print(txt.format(10))

txt = "The Hexadecimal version of {0} is {0:x}"
print(txt.format(255))

txt = "The Hexadecimal version of {0} is {0:X}"
print(txt.format(255))

txt = "You scored {:%}"
print(txt.format(0.25))

txt = "You scored {:.0%}"
print(txt.format(0.25))
