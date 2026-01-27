# METHOD RESOLUTION ORDER
# which method to call if there are multiple methods of same name in classes

class A:
    label = "A"

    def display(self):
        print("Display A")


class B(A):
    label = "B"

    def display(self):
        print("Display B")


class C(A):
    label = 'C'

    def display(self):
        print("Display C")
        

class D(B, C):  # order matters, the first one is explored earlier
    def get(self):
        self.display()
        super().display()
        print(f"Label: {self.label}")
    

obj = D()
obj.get()

# resolves which method or attribute to use