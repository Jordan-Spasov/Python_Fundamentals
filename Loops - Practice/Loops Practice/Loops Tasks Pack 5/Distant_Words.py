t = int(input())
n = int(input())

total_sum = 0

for words in range(n):
    word = input()
    temp_res = 0
    upper_word = word.upper()
    for char in upper_word:
        temp_res += ord(char) - 64
    distance = abs(temp_res - t)
    print(word, distance)
    total_sum += distance
avg_dist = total_sum / n
print(f'{avg_dist:.2f}')