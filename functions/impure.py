arg = 10

def fn():
    global arg 
    arg = 20
    print(arg)
    print("This is an impure function")
    
    
fn()
print(arg)