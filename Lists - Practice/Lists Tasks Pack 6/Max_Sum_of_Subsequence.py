import sys

num = int(input())

temp = 0
max_sum = -sys.maxsize

for i in range(num):
    el = int(input())
    temp = max(el, el + temp)

    max_sum = max(max_sum, temp)

    if temp > max_sum:
        max_sum = temp
print(max_sum)