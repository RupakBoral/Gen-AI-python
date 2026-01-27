def fn():
    
    variable = 'undefined'
    
    def fn1():
        nonlocal variable
        print(f"variable id: {id(variable)}")
    
    def fn2():
        nonlocal variable
        print(f"variable id: {id(variable)}")
        
    print(variable)
    print(f"variable id: {id(variable)}")
    
    return fn1, fn2
        
        
fn1, fn2 = fn()
fn1()
fn2()
        