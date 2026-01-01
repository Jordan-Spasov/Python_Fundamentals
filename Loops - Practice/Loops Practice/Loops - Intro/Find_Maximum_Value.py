num = int(input())

max_num = -200

for i in range(num):
    var = int(input())
    if var > max_num:
        max_num = var
print(max_num)