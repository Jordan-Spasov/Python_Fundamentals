n = int(input())
x = float(input())

factorial = 1
sum = 1

for i in range(1, n + 1):
    factorial *= i
    sum += factorial / (x ** i)
print(f'{sum:.5f}')