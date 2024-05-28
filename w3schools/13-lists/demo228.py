# W3Schools, Python Lists, List Methods
def myFunc(e):
    return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(reverse = True, key = myFunc)

print(cars)
