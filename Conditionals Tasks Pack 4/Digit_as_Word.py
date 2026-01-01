user_input = input()

if user_input.isdigit():
    parse = int(user_input)
    if parse == 0:
        print("zero")
    elif parse == 1:
        print("one")
    elif parse == 2:
        print("two")
    elif parse == 3:
        print("three")
    elif parse == 4:
        print("four")
    elif parse == 5:
        print("five")
    elif parse == 6:
        print("six")
    elif parse == 7:
        print("seven")
    elif parse == 8:
        print("eight")
    elif parse == 9:
        print("nine")
else:
    print("not a digit")