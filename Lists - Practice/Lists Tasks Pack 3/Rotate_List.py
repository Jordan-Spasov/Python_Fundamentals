list = input().split(',')

rotation = int(input())

for rot in range(rotation):
    list = list[1:] + [list[0]]
    join = ','.join(list)
print(join)