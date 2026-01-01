# First solutions

array = input()
s_array = input()

if array < s_array:
    print('first')
elif array > s_array:
    print('second')
else:
    print('equal')

# Second solution

word1 = input()
word2 = input()

list1 = list(word1)
list2 = list(word2)

# Comparing character by character
min_length = min(len(list1), len(list2))

for char in range(min_length):
    if list1[char] < list2[char]:
        print('first')
        break
    elif list1[char] > list2[char]: # to ask why is list1 greater than list 2
        print('second')
        break
else:
    # Checking length 
    if len(list1) < len(list2):
        print('first')
    elif len(list1) > len(list2):
        print('second')
    else:
        print('equal')