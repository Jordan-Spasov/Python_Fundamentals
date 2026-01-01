values = list(map(int, input().split(' ')))

for el in values:
    int_conv= int(el)
    c_to_f = int_conv * 1.8 + 32
    print(round(c_to_f))