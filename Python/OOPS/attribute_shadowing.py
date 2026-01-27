# Attribute shadowing is when an object's property is not provided/ deleted because of which the fallback attribute is used. The fallback attribute is the default value defined in the class.

class Student:
    # attributes
    name: str | None = 'Student'
    id: int | None = '0'
    section: int | None = '0'

    # methods
    def __init__(self):
        name = input("Enter the name of the student: ")
        id = input("Enter the id of the student: ")
        section = input("Enter the section of the student ")

        if(name): self.name = name
        if(id): self.id = id
        if(section): self.section = section

        del self.id  # we are deleting the object's id value

    def __str__(self):
        return f"Name of the student: {self.name}, Id: {self.id}, Section: {self.section}"


def main():
    stud1 = Student()
    print(stud1)
    Student.__str__(stud1) # passing the object


main()