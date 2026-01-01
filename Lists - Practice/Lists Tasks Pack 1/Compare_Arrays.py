num = int(input())

list1 = []
list2 = []

flag = True

for list in range(num):
    list1.append(input())
for list in range(num):
    list2.append(input())
for i in range(num):
    if list1[i] != list2[i]:
        flag = False
        break
if flag:
    print('equal')
else:
    print('not equal')