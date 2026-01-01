num = int(input())

for wave in range(0, num):
    print(wave + 1, end = ' ')
    temp_var = num
for wave2 in range(1, num):
    temp_var -= 1
    print(temp_var, end = ' ')