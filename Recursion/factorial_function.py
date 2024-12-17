def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n - 1)

# O(n) number of operations, as there are n + 1 activations, each of which accounts for O(1) operations.
print(factorial(5))