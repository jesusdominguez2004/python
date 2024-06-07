# W3Schools, Python JSON
import json

x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

y = json.dumps(x)

print(y)
print(type(y))  # class 'str'
