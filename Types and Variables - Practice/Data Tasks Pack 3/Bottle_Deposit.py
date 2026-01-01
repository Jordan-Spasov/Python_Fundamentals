# half liter = 0.1
# one liter = 0.25

half_liter = int(input())
one_liter = int(input())

half_liter_sum = half_liter * 0.1
one_liter_sum = one_liter * 0.25
total = half_liter_sum + one_liter_sum
print(f'{total:.2f}')