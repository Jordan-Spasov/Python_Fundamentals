A = input()
B = input()

if A > B:
    temp = A
    A = B
    B = temp

print(A, B)