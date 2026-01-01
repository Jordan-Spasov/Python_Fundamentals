num = int(input())

list = []
max_seq = 0
count = 0

for longseq in range(num):
    list.append(int(input()))

bucket = []

for loop in list:
    if bucket == loop:
        count += 1
        if count >= max_seq:
            max_seq = count
    else:
        bucket = loop
        count = 1
print(max_seq)