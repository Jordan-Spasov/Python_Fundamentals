# First solution
num = int(input())

output = ''

for i in range(1, num + 1):
    output += str(i) + ' '
print(output, end = '')

# Second solution
n = int(input())

x = 1
output= ''

while x <= n:
    output += str(x)
    x += 1
print(output, end = '')