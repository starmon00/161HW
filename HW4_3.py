def k_small(A, B, k):
    n = len(A)
    m = len(B)
    # Handle base cases.
    if n == 0:
        return B[k - 1]
    if m == 0:
        return A[k - 1]
    if n + m == k:
        if A[n - 1] < B[m - 1]:
            return B[m - 1]
        else:
            return A[n - 1]
    # Set starting indices
    i = min((n - 1) / 2, k - 1)
    j = k - 1 - i
    # Cap j if too big
    if j >= m:
        j = m - 1
        i = k - 1 - j
    # Recurse
    if A[i] <= B[j]:
        if j == 0:
            return A[i]
        elif B[j - 1] <= A[i]:
            return A[i]
        else:
            return k_small(A[i:n], B[0:j], k - i)
    else:
        if i == 0:
            return B[j]
        elif A[i - 1] <= B[j]:
            return B[j]
        else:
            return k_small(A[0:i], B[j:m], k - j)
