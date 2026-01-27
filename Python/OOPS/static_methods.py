# Static methods are called without objects
# A static method does not receive an implicit first argument.


class A:
    @staticmethod
    def fn():
        print("Class A")

    
A.fn()


# Takes no self or cls

# Cannot access instance or class variables directly

# Used for helper / utility logic

# Independent of class state