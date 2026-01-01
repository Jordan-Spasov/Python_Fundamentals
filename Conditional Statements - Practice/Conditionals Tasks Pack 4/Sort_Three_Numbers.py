num1 = int(input())
num2 = int(input())
num3 = int(input())

#first = -1000
#second = -1000
#third = -1000

if num1 >= num2 and num1 >= num3:
    if num2 >= num3:
        print(num1, num2, num3)
    else:
        print(num1, num3, num2)
elif num2 >= num1 and num2 >= num3:
    if num1 >= num3:
        print(num2,num1, num3)
    else:
        print(num2, num3, num1)
else:
    if num2 >= num1:
        print(num3, num2, num1)
    else:
        print(num3, num1, num2)