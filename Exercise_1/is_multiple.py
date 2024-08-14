# Write a short Python function, is multiple(n, m),
# that takes two integer values and returns True if n is a multiple of m,
# that is, n = mi for some integer i, and False otherwise.

def is_multiple(n: int,
                m: int) -> bool:
    while n and m > 0:
        return n % m == 0

print(is_multiple(21, 0))