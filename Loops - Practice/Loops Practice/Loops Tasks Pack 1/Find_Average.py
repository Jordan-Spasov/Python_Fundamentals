num = int(input())

sum_nums = 0

for i in range(num):
    number = float(input())
    sum_nums += number
print(f'{sum_nums / num:.2f}')