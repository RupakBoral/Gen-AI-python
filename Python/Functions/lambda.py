demand_fruits = ['apple', 'mango', 'orange', 'pineapple', 'tomato']
onstock_fruits = ['apple', 'orange', 'tomato']

available_fruits = list(filter(lambda fruit : fruit in onstock_fruits, demand_fruits))

print(available_fruits)