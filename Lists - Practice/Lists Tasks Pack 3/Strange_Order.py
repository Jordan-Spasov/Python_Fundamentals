num = input().split(',')

neg_num = []
zeros = []
positives = []

for strange in num:
    if int(strange) < 0:
        neg_num.append(strange)
    elif int(strange) == 0:
        zeros.append(strange)
    else:
        positives.append(strange)
conc = neg_num + zeros + positives
print(','.join(conc))