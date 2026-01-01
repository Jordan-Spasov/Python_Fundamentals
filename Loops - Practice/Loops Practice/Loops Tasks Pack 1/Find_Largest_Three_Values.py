num = int(input())

first = -500
second = -500
third = -500

for i in range(num):
    n = int(input())
    if n > first:
        third = second
        second = first
        first = n
    elif n >= second:
        third = second
        second = n
    elif n > third:
        third = n
print(f'{first}, {second} and {third}')