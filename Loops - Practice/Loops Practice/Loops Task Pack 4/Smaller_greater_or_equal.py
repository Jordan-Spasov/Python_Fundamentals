num = int(input())
f_num = int(input())
output = str(f_num)

for i in range(num - 1):
    next_num = int(input())

    if f_num == next_num:
        output += "="
    elif f_num > next_num:
        output += ">"
    else:
        output += "<"

    output += str(next_num)
    f_num = next_num
print(output)