nums = input().split(' ')

pos_list = []
neg_list = []

for sort in nums:
    sort = int(sort)
    if sort < 0:
        neg_list.append(sort)
    if sort >= 0:
        pos_list.append(sort)
print(*neg_list, *pos_list)