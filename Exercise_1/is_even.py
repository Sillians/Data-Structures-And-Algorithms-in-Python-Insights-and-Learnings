# Write a short Python function, is even(k), that takes an integer value and returns
# True if k is even, and False otherwise.
# However, your function cannot use the multiplication, modulo, or division operators.

# argument = k
# return k if even
# return False if otherwise

def is_even(k):
    if k & 1 == 0:
        return True
    return False

k = 101
print(is_even(k))