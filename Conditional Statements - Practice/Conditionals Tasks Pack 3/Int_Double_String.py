var_type = input()
var_value = input()

increasement = 0

if var_type == 'integer':
    increasement = 1
    sum_plus_inc = int(var_value) + increasement
    print(sum_plus_inc)
elif var_type == 'real':
    increasement = 1
    sum_plus_inc = float(var_value) + increasement
    print(f'{sum_plus_inc:.2f}')
else:
    print(var_value + '*')