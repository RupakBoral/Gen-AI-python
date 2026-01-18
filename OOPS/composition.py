# In composition, we create objects of a class inside the class, instead of inheriting the class.
# Composition = has-a

class Engine:
    def __init__(self, horse_power):
        self.horse_power = horse_power


class Wheel:
    def __init__(self, size):
        self.size = size


class Car:
    def __init__(self, brand, model, horse_power, size):
        self.brand = brand
        self.model = model
        self.engine = Engine(horse_power=horse_power) # engine has reference of Engine object
        self.wheel = Wheel(size=size)
    
    def get(self):
        print(f"Brand {self.brand}, Model: {self.model}, Horse power: {self.engine.horse_power} hp, Wheel size: {self.wheel.size} inch")


car = Car("Porshe", "911", 450, 20)
car.get()

