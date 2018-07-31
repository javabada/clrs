def insertion_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        # to sort in reverse: A[i] < key
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key


A = [5, 2, 4, 6, 1, 3]

print('Array before:')
print(A)

insertion_sort(A)

print('Array after:')
print(A)
