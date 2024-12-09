class Vehicle():
    def __init__(self, wheels, max_speed):
        self.wheels = wheels
        self.max_speed = max_speed

    def drive(self):
        print(f"Going {self.max_speed} with my {self.wheels} wheels")

class Bike(Vehicle):
    def __init__(self, max_speed, weight):
        Vehicle.__init__(self, 2, max_speed)
        self.weight = weight

class Car(Vehicle):
    def __init__(self, max_speed, seats):
        Vehicle.__init__(self, 4, max_speed)
        self.seats = seats

class Convertible(Car):
    def __init__(self, max_speed, foldable_roof):
        Car.__init__(self, max_speed, 2)
        self.foldable_roof = foldable_roof


list_of_vehicles = [
    Bike(215, 138),
    Car(200, 4),
    Convertible(190, True)
]

for v in list_of_vehicles:
    v.drive()
    if type(v) is Convertible:
        print(v.foldable_roof)
    if isinstance(v, Car):
        print (v.seats)