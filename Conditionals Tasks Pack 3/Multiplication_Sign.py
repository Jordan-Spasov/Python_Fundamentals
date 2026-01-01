num1 = float(input())
num2 = float(input())
num3 = float(input())

if num1 == 0 or num2 == 0 or num3 == 0:
    print("0")
else:
    negative_count = 0
    
    if num1 < 0:
        negative_count += 1
    elif num2 < 0:
        negative_count += 1
    elif num3 < 0:
        negative_count += 1

    elif negative_count % 2 == 0:
        print("+")
    else:
        print("-")