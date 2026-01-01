num = int(input())

count = 0

for i in range(1, num + 1):
    count += 1
    print()
    for j in range(0, num):
        print(f'{j + count}', end = ' ')