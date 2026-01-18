class Person:
    def __init__(self, age=None):
        self._age = age

    @property
    # age getter
    def age(self):
        return f"The age is: {self._age}"
    
    @age.setter
    # age setter
    def age(self, age):
        try:
            if age >= 18:
                self._age = age
                return "Eligible to vote"
            else:
                raise ValueError("Ineligible to vote, age is less than 18")
        except Exception as ex:
            print(f"Exception: {ex}")


person1 = Person()
age = int(input("Enter the age of the voter: "))

person1.age = age

if person1.age is not None: print(person1.age)