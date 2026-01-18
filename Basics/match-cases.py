val = int(input("Enter a value"))
rem = val % 2

match rem:
    case 0:
        print("The value is even")
    
    case 1:
        print("The value is odd")