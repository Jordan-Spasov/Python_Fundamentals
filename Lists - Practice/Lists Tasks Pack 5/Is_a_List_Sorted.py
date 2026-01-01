num = int(input())

for numb in range(num):
    x = 'true'
    line = input().split(',')
    first = int(line[0])
    for value in range(1, len(line)):
        if int(line[value]) < int(line[value - 1]):
            x = 'false'
    print(x)