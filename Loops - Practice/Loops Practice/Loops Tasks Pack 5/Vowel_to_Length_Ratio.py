all_vow = 'aouei'

num = int(input())

best_word = ""
ratio = 1
max_vol_count = 0

for i in range(num):
    word = input()
    vowels_in_word = 0
    for char in word:
        if char in all_vow:
            vowels_in_word += 1

    if vowels_in_word / len(word) < ratio:
        best_word = word
        max_vol_count = vowels_in_word
        ratio = vowels_in_word / len(word)

    elif vowels_in_word / len(word) == ratio and vowels_in_word == max_vol_count and len(best_word) < len(word):
        best_word = word
        max_vol_count = vowels_in_word
        ratio = vowels_in_word / len(word)

    elif vowels_in_word / len(word) == ratio and vowels_in_word > max_vol_count:
        best_word = word
        max_vol_count = vowels_in_word
        ratio = vowels_in_word / len(word)
    
print(f'{best_word} {max_vol_count}/{len(best_word)}')