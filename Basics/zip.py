# zip function is used to combine multiple iterable

names = ["Harry", "Boston", "Rick", "Sarah"]
ages =  [21, 20, 17, 23]

for name, age in zip(names, ages):
    print(f"Name: {name}, Ages: {age}")


