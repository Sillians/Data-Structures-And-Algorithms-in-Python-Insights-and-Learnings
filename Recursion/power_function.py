# Runs in O(n) time
def power(x: float, n: int):
    """Compute the value x**n for integer n."""
    if n == 0:
        return 1
    else:
        return x * power(x, n-1)

x = 2
n = 3
print(power(x, n))

## Squaring technique, runs in `O(log n)`
def power2(x: float, n: int):
    """Compute the value x**n for integer n."""
    if n == 0:
        return 1
    else:
        partial = power2(x, n // 2)  # rely on truncated division
        result = partial * partial
        if n % 2 == 1:     # if n is odd, include extra factor of x
            result *= x
        return result

x = 2
n= 13
print(power2(x, n))