"""R-1.4 Write a short Python function that takes a positive
integer n and returns the sum of the squares of all the positive integers smaller than n.
"""

def sum_squares(n: int) -> int:
  # check if n is an integer
  if n >= 0 and isinstance(n, int):
    sum_values = []

    for integers in range(1, n):
      sum_values.append(integers**2)
    return sum(sum_values)
  else:
    return("The value of n must be a positive integer")


def sum_of_squares(n: int) -> int:
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")

    return sum(i ** 2 for i in range(1, n))


n = 5
result = sum_of_squares(n)
print(result)


"""
Write a short Python function that takes a positive integer n and 
returns the sum of the squares of all the odd positive integers smaller than n.
"""

def sum_of_odd_squares(n: int) -> int:
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")

    sum_odd_squares = []
    for i in range(1, n):
        if i % 2 != 0:
            sum_odd_squares.append(i**2)
    return sum(sum_odd_squares)

def sum_of_odd_squares2(n: int) -> int:
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")

    return sum([i**2 for i in range(1, n) if i%2!=0])

n = 5
result = sum_of_odd_squares2(n)
print(result)