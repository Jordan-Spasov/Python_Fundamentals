list = input().split(',')

my_set = []

for el in list:
    if not el in my_set:
        my_set.append(el)
print(','.join(my_set))