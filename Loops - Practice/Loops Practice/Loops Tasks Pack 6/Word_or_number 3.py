num = int(input())

num_sum = 0
conc_text = ""
temp = input()
counter = num - 1 

while counter:

    line = input()
    counter -= 1

    if temp[-1].isdigit() and line[-1].isdigit():
        temp = str(int(temp) + int(line))

    elif temp[-1].isdigit() and line[-1].isalpha():
        print(temp)
        temp = line

    elif temp[-1].isalpha() and line[-1].isalpha():
        temp += "-" + line

    elif temp[-1].isalpha() and line[-1].isdigit():
        print(temp)
        temp = line

    elif not line.isalnum():
        print(temp)
        print(line)
        temp = input()
        counter -= 1
        
print(temp)