from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")
    return wrapper

@my_decorator
def greet():
    print("This is a greeting message")


greet()
print(greet.__name__) # without wraps --> wrapper is the name


# so basically, I am passing my function (greet) to my_decorator function, which consist of a wrapper function which will eventually execute my greet function