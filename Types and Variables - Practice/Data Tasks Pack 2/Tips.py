import math

meal_price = int(input())
# tip = 10$ of meal price

tip = meal_price * 0.1
total_price = math.trunc(meal_price + tip)

print(total_price)