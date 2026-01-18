# Inheritance = is-a

class Parent:
    property: str
    car: str

class Child(Parent):
    job: str
    identity: str
    respect: str

    def __str__(self):
        return f"Property: {self.property}, Car: {self.car}, Job: {self.job}, Identity: {self.identity}, Respect: {self.respect}"


child = Child()
child.property = "Property"
child.car = "Car"
child.job = "Job"
child.identity = "Identity"
child.respect = "Respect"


print(child)