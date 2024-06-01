# W3Schools, Python Arrays
def myFunc(e):
    return e['year']

cars = [
    {'car': 'Ford', 'year': 2005},
    {'car': 'Mitsubishi', 'year': 2000},
    {'car': 'BMW', 'year': 2019},
    {'car': 'VW', 'year': 2011}
]

cars.sort(key = myFunc)
print(cars)

# Python does not have built-in support for Arrays, 
# but Python Lists can be used instead.

