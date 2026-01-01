num = int(input())

yes_or_no = []

for symm in range(num):
    num_var = input().split()
    is_palindromic = True
    for diff in range(len(num_var) // 2):
        if num_var[diff] != num_var[len(num_var) - diff - 1]:
            is_palindromic = False
            break
    if is_palindromic:
        yes_or_no.append('Yes')
    else:
        yes_or_no.append('No')
for res in yes_or_no:
    print(res)