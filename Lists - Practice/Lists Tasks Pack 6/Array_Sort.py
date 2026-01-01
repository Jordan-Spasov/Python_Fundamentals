lst = input().split(',')

nums = []
zeros = []

for el in lst:
    if el == '0':
        zeros.append(el)
    else:
        nums.append(el)
print(','.join(nums + zeros))