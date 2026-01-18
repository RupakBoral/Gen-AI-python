# 
# Scopes:
# 1. Global
# 2. Local
# 3. Enclosing
# 4. Built in
#

scope = "global"

def fn1():
    scope = "local 1"
    print(f"Inside function 1: {scope}")
    
def fn2():
    scope = "local 2"
    print(f"Inside function 2: {scope}")
    print(id(scope))
    
    def fn3():
        print(f"Enclosing scope: Inside function 3: {scope}")
        print(id(scope))
        
    return fn3

print(f"Global scope: {scope}")

fn1()

fn2()()


# Enclosing scope is using scope of outer function, like fn3 uses scope variable of fn2