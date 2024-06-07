# W3Schools, Python JSON
import json

x = '{"name":"John", "age":30, "city":"New York"}'

y = json.loads(x)

print(y["age"])
print(type(y))  # class 'dict'
