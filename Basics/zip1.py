# zip function is used to combine multiple iterable

names = ["Harry", "Boston", "Rick", "Sarah"]
ages =  [21, 20, 17, 23]

for name, age in zip(names, ages):
    print(f"Name: {name}, Ages: {age}")


food = ["cornflakes", "briyani", "roti & panner"] 
time = ("breakfast", "lunch", "dinner")

for time, food in zip(time, food):
    print(f"At {time}: {food}")
    
    
    
# zip works for both lists and tuple 