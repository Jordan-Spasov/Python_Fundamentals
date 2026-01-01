c_s = input()

suit1 = "spades"
suit2 = "clubs"
suit3 = "hearts"
suit4 = "diamonds"

if c_s == 'J' or c_s == 'Q' or c_s == 'K' or c_s == 'A':
    for i in range(2, 11):
        print(f'{i} of {suit1}, {i} of {suit2}, {i} of {suit3}, {i} of {suit4}')
    print(f'J of {suit1}, J of {suit2}, J of {suit3}, J of {suit4}')
    
    if c_s == 'A':
        print('Q of {suit1}, Q of {suit2}, Q of {suit3}, Q of {suit4}')
        print('K of {suit1}, K of {suit2}, K of {suit3}, K of {suit4}')
        print('A of {suit1}, A of {suit2}, A of {suit3}, A of {suit4}')
    elif c_s == 'K':
        print('Q of {suit1}, Q of {suit2}, Q of {suit3}, Q of {suit4}')
        print('K of {suit1}, K of {suit2}, K of {suit3}, K of {suit4}')
    elif c_s == 'Q':
        print('Q of {suit1}, Q of {suit2}, Q of {suit3}, Q of {suit4}')

else:
    c_s = int(c_s)
    for i in range(2, c_s + 1):
        print(f'{i} of spades, {i} of clubs, {i} of hearts, {i} of diamonds')