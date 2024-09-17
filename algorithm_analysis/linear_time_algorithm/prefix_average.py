def prefix_average3(S: list):
    n = len(S)
    A = [0] * n                    # create new list of n zeros
    total = 0                      # compute prefix sum as S[0] + S[1] + ...
    for j in range(n):
        total += S[j]              # update prefix sum to include S[j]
        A[j] = total / (j + 1)     # compute average based on current sum
    return A

arr = [2, 4, 6, 8, 5]
print(prefix_average3(arr))