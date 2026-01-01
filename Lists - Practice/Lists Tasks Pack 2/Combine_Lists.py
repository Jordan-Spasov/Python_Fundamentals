list1 = list(map(int, input().split(',')))
list2 = list(map(int, input().split(',')))

output = []

for array in range(len(list1)):
    output.append(str(list1[array]))
    output.append(str(list2[array]))
print(','.join(output))