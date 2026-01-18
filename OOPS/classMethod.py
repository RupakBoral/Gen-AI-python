# A class method is a method that is bound to the class, not to an individual object.
# It receives the class itself as the first parameter, conventionally named cls.
# Self is instance of the class

class A:
    def __init__(self, taste, quantity):
        self.taste = taste
        self.quantity = quantity

    @classmethod
    def input_from_string(cls, string_input):
        taste, quantity = string_input.split(', ')
        return cls(taste, quantity)
    
    @classmethod
    def input_from_dict(cls, dict_input):
        taste = dict_input['taste']
        quantity = dict_input['quantity']
        return cls(taste, quantity)
    
    def __str__(self):
        return f"taste: {self.taste}, quantity: {self.quantity}"


obj1 = A.input_from_dict({"taste": "sweet", "quantity": 100})
obj2 = A.input_from_string("sour, 20")

print(obj1.__dict__)
print(obj2.__dict__)

# Takes cls as the first parameter
# Can access and modify class variables
# Knows which class is calling it
# Often used as alternative constructors
