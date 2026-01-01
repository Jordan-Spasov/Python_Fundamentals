num = int(input())

numbers = []

for rep in range(10):
    numbers.append(0)

for i in range(num):
    next_num = int(input())
    numbers[next_num - 1] += 1

max_value = max(numbers)
best_num = 10

for iter in range(10):
    if numbers[iter] == max_value and best_num > iter + 1:
        best_num = iter + 1
print(best_num)