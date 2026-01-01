num_sort = input().split(', ')

list = []

for el in num_sort:
    list.append(int(el))

sort = sorted(list, reverse = True)

empty_list = []

for el in sort:
    empty_list.append(str(el))
    
print(','.join(empty_list))