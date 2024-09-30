# Linear function O(n) times
def prefix_average3(S: list):
    n = len(S)      # O(1) time
    A = [0] * n     # O(n) time               # create new list of n zeros
    total = 0       # O(1) time               # compute prefix sum as S[0] + S[1] + ...
    for j in range(n): # O(n) time
        total += S[j]  # O(n) time            # update prefix sum to include S[j]
        A[j] = total / (j + 1)  # O(n) time   # compute average based on current sum
    return A

arr = [2, 4, 6, 8, 5]
print(prefix_average3(arr))