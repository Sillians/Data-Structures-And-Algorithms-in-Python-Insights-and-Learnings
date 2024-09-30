# If each of the original sets has size n, then the worst-case running time of this function is O(n^3).
def disjoint1(A: list, B: list, C: list) -> bool:
    """Return True if there is no element common to all three lists."""
    for a in A:
        for b in B:
            for c in C:
                if a == b == c:
                    return False   # we found a common value
    return True                    # if we reach this, sets are disjoint

A = [6, 4, 5, 6, 7, 8]
B = [2, 3, 5, 7, 8, 9]
C = [1, 4, 2, 6, 2, 3]

print(disjoint1(A, B, C))


"""
We can improve upon the asymptotic performance with a simple observation. 
Once inside the body of the loop over B, if selected elements a and b do not match each other, 
it is a waste of time to iterate through all values of C looking for a matching triple. 
An improved solution to this problem, taking advantage of this observation, is:
"""
# the total time spent is O(n^2).
def disjoint2(A: list, B: list, C: list) -> bool:
    for a in A:
        for b in B:
            if a == b:                # only check C if we found match from A and B
                for c in C:
                    if a == c:        # (and thus a == b == c)
                        return False  # we found a common value
    return True                       # if we reach this, sets are disjoint

print(disjoint2(A, B, C))



























