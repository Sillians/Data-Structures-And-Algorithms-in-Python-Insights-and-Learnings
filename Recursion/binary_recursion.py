def binary_sum(S: list, start: int, stop: int):
    """Return the sum of the numbers in implicit slice S[start:stop]."""
    if start >= stop:           # zero elements in slice
        return 0
    if start == stop - 1:       # one element in slice
        return S[start]
    else:
        mid = (start + stop) // 2
        return binary_sum(S, start, mid) + binary_sum(S, mid, stop)


S = [4, 3, 6, 2, 8]
start = 0
stop = len(S)
print(binary_sum(S, start, stop))