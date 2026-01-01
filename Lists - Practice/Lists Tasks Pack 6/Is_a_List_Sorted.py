num = int(input())

for numb in range(num):
    x = True
    line = input().split(',')
    first = int(line[0])
    for value in line[1]:
        if value < value[0]:
            