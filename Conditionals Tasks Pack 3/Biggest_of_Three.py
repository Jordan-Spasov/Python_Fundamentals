# First solution
num1 = int(input())
num2 = int(input())
num3 = int(input())

bigg = max(num1, num2, num3)
print(bigg)

# Another way
a = int(input())
b = int(input())
c = int(input())

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c
print(largest)