# function
def fn1():
    return ["Cup 1", "Cup 2", "Cup 3"]

# generator
def fn2():
    yield "Cup 1"
    yield "Cup 2"
    yield "Cup 3"


res1 = fn1()
print(res1)

print("----------------------------------")

res2 = fn2() # object of generator fn2 reference to the address of the generator
# print(res2)   # res is pointing to start of function before the yield

# printing the values 
while(res2):
    try:
        print(next(res2))
    except Exception:
        break