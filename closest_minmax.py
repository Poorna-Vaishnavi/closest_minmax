def smallest_subarray_size(A):
    max_val = max(A)
    min_val = min(A)
    min_max_indices = []

    for i in range(len(A)):
        if A[i] == max_val or A[i] == min_val:
            min_max_indices.append(i)

    return min_max_indices[-1] - min_max_indices[0] + 1


A = list(map(int, input("Enter the elements of array A : ").split()))

output = smallest_subarray_size(A)
print("Size of the smallest subarray:", output)