num = int(input())

min_num = 10000
max_num = -10000
sum_num = 0
avg_num = 0

for n in range(num):
    n = float(input())
    if n > max_num:
        max_num = n
    if n < min_num:
        min_num = n
    sum_num += n
avg_num = sum_num / num

print(f"min={min_num:.2f}")
print(f"max={max_num:.2f}")
print(f"sum={sum_num:.2f}")
print(f"avg={avg_num:.2f}")