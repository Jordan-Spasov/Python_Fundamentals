r = ord(input()) - 96
l = int(input())

if (r % 2) == (l % 2):
    print('dark')
else:
    print('light')