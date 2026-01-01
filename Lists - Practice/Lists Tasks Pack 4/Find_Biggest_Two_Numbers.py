nums_in_string = input().split(' ')

nums_list = []

for num in nums_in_string:
    nums_list.append(int(num))
    
nums_list = sorted(nums_list, reverse = True)[:2]

for nums in nums_list:
    print(nums, end = ' ')