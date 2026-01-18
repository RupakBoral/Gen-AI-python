food = ["cornflakes", "briyani", "roti & panner"] 
time = ("breakfast", "lunch", "dinner")

for time, food in zip(time, food):
    print(f"At {time}: {food}")
    
    
    
# zip works for both lists and tuple 