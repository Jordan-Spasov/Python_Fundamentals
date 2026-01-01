input = input()

if '0' <= input[-1] <= '9':
    temp = float(input) // 1
    if float(input) - temp == 0:
        print(int(input) + 1)
    else:
        print(float(input) + 1)
else:
    for i in range(len(input)):
        print(input[-1-i], end='')