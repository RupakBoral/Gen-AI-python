from functools import wraps

def logging(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Going for a ride on {args[0]}")
        res = func(*args, **kwargs)
        print(f"Finished the ride on {args[0]}")
        return res
    return wrapper


@logging
def ride_car(car):
    print(f"Riding {car}")
    return None


ride_car("Mercedes M1")
