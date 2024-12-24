def binary_search_iterative(data: list, target: int):
    """Return True if target is found in the given Python list"""
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:            # found a match
            return True
        elif target < data[mid]:
            high = mid - 1                 # only consider values left of mid
        else:
            low = mid + 1                  # only consider values right of mid
    return False                           # loop ended without success


target = 5
data = [0, 2, 4, 5, 6, 8, 9, 12, 45, 56, 78, 83, 99]
print(binary_search_iterative(data, target))



def reverse_iterative(S):
    """Reverse elements in sequence S."""
    start, stop = 0, len(S)
    while start < stop - 1:
        S[start], S[stop - 1] = S[stop - 1], S[start]           # swap first and last
        start, stop = start + 1, stop - 1                      # narrow the range


S = [4, 3, 6, 2, 8]
print(reverse_iterative(S))
