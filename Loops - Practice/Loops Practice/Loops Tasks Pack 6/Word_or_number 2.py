num = int(input())

numb = 0
text = ''

for word in range(num):
    user_input = input()
    if user_input.isdigit():
        numb += int(user_input)
    else:
        text += user_input + '-'
if not text:
    text = 'no words'
print(text.strip('-'))
print(numb)