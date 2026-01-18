foods = ["momo", "dosa", "samosa", "briyani", "fried rice", "momo", "samosa"]

unique_food_set = {food for food in foods}
unique_food_list = [food for food in foods]

# print(unique_food_set)
# print(unique_food_list)


myEat = {
    "breakfast": ["cornflakes", "bread-butter", "bread-omlette"],
    "lunch": ["chole-bhature", "roti-sabzi", "briyani"],
    "dinner": ["briyani", "fried rice", "roti-sabzi"],
    "desert": ["ice-crean", "gulab-jamun", "rasmalai"]
}

# If I want set of all the food
myFood = {food for listOfFood in myEat.values() for food in listOfFood}
print(myFood)

# If I want set of my timings
myTiming = {time for time in myEat.keys()}
print(myTiming)