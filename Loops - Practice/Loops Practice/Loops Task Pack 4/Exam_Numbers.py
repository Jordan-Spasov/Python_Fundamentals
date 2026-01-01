# You want to find all the 3-digit numbers that are in some interval and whose sum of digits equal some target

x = int(input())
y = int(input())
t = int(input())

for num in range(x, y + 1):
    conv = str(num)
    digit = int(conv[0]) + int(conv[1]) + int(conv[2])
    if digit == t:
        print(num)