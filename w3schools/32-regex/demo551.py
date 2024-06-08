# W3Schools, Python RegEx
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())
