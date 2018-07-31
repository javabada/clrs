def linear_search(A, v):
    for i in range(0, len(A)):
        if A[i] == v:
            return i
    return None


A = [5, 2, 4, 6, 1, 3]
v1 = 4
v2 = 8
i1 = linear_search(A, v1)
i2 = linear_search(A, v2)

print('Array:')
print(A)
print('Value {} found at index {}'.format(v1, i1))
print('Value {} found at index {}'.format(v2, i2))
