"""
In the former, we are given three collections and we presumed that there were no duplicates within a single collection.
In the element uniqueness problem, we are given a single sequence S with n elements and asked whether all elements of that collection are distinct from each other.

"""
# Bruce-force implementation
def unique(S: list) -> bool:
    n = len(S)
    for i in range(n):
        if S.count(S[i]) > 1:
            return False
    return True

S = [4, 3, 2, 1, 8, 5, 3]
print(unique(S))

# O(n^2) time complexity
def unique1(S: list) -> bool:
    """Return True if there are no duplicate elements in sequence S."""
    for j in range(len(S)):
        for k in range(j+1, len(S)):
            if S[j] == S[k]:
                return False
    return True

print(unique1(S))

# worst-case running time of O(nlogn)
def unique2(S: list) -> bool:
    sorted_list = sorted(S)                    # create a sorted copy of S
    for j in range(1, len(sorted_list)):
        if sorted_list[j-1] == sorted_list[j]:
            return False                       # found duplicate pair
    return True                                # if we reach this, elements were unique

print(unique2(S))












