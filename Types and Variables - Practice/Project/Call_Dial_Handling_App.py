p_one = '01.Potato'
p_two = '02.Fish'
p_three = '03.Apple'

voice_msg = 'Menu: Dial only one digit: 1 - Create Order: '
print(voice_msg)

user_input = int(input())

print(f'Here are our products: {p_one}, {p_two}, {p_three}')

p_code = input('Enter the 2 digit product code to add it to the order:')
print(f'Product with code: {p_one} was added to the order')

p_code2 = int(input('Enter the 2-digit product code to add it to the order:'))
print(f'Product with code: {p_two} was added to the order')

p_code3 = input('Enter the 2-digit product code to add it to the order:')
print(f'Product with code: {p_three} was added to the order')

print()

thanks_var = 'Thank you for using our program!'
print(thanks_var)
summary_var = 'Summary of your interaction:'
print(summary_var)

print(f'Orders: 1 order containing {p_code}, {p_code2}, {p_code3}')