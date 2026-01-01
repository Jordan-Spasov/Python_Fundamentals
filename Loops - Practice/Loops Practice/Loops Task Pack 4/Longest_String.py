food_name = input()

best_food_name = ''
best_food_name_length = 0

while food_name != 'END':
    if len(food_name) >= best_food_name_length:
        best_food_name_length = len(food_name)
        best_food_name = food_name
    food_name = input()
print(best_food_name)