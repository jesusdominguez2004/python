# W3Schools, Python Lists, List Methods
def myFunc(e):
    return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(key = myFunc)

print(cars)
