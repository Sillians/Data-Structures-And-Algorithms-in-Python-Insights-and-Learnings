def reverse_sequence(S: list, start: int, stop: int):
    """Reverse elements in implicit slice S[start:stop]"""
    if start < stop - 1:    # If at least 2 elements
        S[start], S[stop - 1] = S[stop - 1], S[start]     # swap first and last
        return reverse_sequence(S, start+1, stop-1)     # recur on rest


S = [4, 3, 6, 2, 8, 9, 5]
start = 0
stop = len(S)
reverse_sequence(S, start, stop)