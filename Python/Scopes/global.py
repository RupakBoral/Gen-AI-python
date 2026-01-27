var = 10
print(id(var))

def fn1():
    def fn2():
        global var 
        var = 10
        print(id(var))
    fn2()
    
fn1()