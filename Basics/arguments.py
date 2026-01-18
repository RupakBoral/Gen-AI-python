# Lists

# brands = ['addidas', 'puma', 'reebok', 'nike', 'december']

# def edit_brands(brands):
#     brands.remove('december')
    
# print(f"Before editing {brands}")
# edit_brands(brands)
# print(f"After editing {brands}")

# single value arg
def fn1(arg):
    print(f"Value {args}")
    print(f"Type: {type(args)}")
    
# takes all the values and wraps in a tuple
def fn2(*args):
    print(f"Value {args}")
    print(f"Type: {type(args)}")
    

# takes the key-value args    
def fn3(**kwargs):
    print(f"Value {args}")
    print(f"Type: {type(args)}")
    
fn1('python')
fn2('python', 'C++', 'JS')
fn3(language='python', name='file')