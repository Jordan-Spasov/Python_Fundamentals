list = input().split(',')

lst = []
above = []
below = []

for baa in list:
    lst.append(int(baa))
avg_sum = sum(lst) / len(lst)

for el in list:
    if int(el) < avg_sum:
        below.append(el)
    elif int(el) > avg_sum:
        above.append(el)
print(f'avg: {avg_sum:.2f}')
print("below:", ",".join(map(str, below)))
print("above:", ",".join(map(str, above )))