def binary_addition(A, B):
    # assumes A and B are of the same length
    C = [None] * (len(A) + 1)
    carry = 0
    # start from the rightmost digit
    for i in range(len(A) - 1, -1, -1):
        C[i + 1] = (A[i] + B[i] + carry) % 2
        carry = (A[i] + B[i] + carry) // 2
    C[0] = carry
    return C


A = [1, 0, 1, 1]
B = [1, 0, 1, 0]
C = binary_addition(A, B)

print('Arrays:')
print(A)
print(B)
print('Result:')
print(C)
