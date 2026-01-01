num = int(input())

for i in range(num):
    price = float(input())
    discount = price * 0.35
    print(f"{discount:.2f}")