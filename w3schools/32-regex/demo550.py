# W3Schools, Python RegEx
import re

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x)    # this will print an object
print(type(x))
