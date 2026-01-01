h_y = int(input())

if h_y <= 2:
    d_y = h_y * 10
    print(d_y)
elif h_y > 2:
    d_y = 20 + ((h_y - 2) * 4)
    print(d_y)