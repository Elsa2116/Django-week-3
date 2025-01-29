# Base Class
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def describe(self):
        return f"Vehicle Make: {self.make}, Model: {self.model}"


# Subclass for Car
class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self.num_doors = num_doors  # Public attribute

    def describe(self):
        return f"Car Make: {self.make}, Model: {self.model}, Doors: {self.num_doors}"


# Subclass for Bike
class Bike(Vehicle):
    def __init__(self, make, model, has_gears):
        super().__init__(make, model)
        self.has_gears = has_gears

    def describe(self):
        gear_status = "with gears" if self.has_gears else "without gears"
        return f"Bike Make: {self.make}, Model: {self.model}, {gear_status}"


# Demonstrate polymorphism
vehicles = [
    Car("Toyota", "Corolla", 4),
    Bike("Yamaha", "YZF", True),
    Vehicle("Generic", "Model-X"),
]

for vehicle in vehicles:
    print(vehicle.describe())
