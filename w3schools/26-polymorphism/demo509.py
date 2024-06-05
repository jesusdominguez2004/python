# W3Schools, Python Polymorphism
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        return "Move!"
    
    def show(self):
        return f"Brand: {self.brand} Model: {self.model}"

class Car(Vehicle):
    def move(self):
        x = super().move()
        return f"{x} And drive!"

class Boat(Vehicle):
    def move(self):
        x = super().move()
        return f"{x} And sail!"

class Plane(Vehicle):
    def move(self):
        x = super().move()
        return f"{x} And fly!"

def main():
    car1 = Car("Ford", "Mustang")
    boat1 = Boat("Ibiza", "Touring 20")
    plane1 = Plane("Boeing", "747")

    for x in (car1, boat1, plane1):
        print(x.show())
        print(x.move())
        print("")

main()
