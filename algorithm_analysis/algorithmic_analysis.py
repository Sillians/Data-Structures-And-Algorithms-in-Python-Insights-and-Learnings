# The algorithm, find_max, for computing the maximum element of a list of n numbers, runs in O(n) time.
def find_max(data_list: list):
    """Return the maximum element from a nonempty Python list."""
    max_num = data_list[0]             # The initial value to beat
    for val in data_list:              # For each value:
        if val > max_num:         # if it is greater than the best so far,
            max_num = val         # we have found a new best (so far)
    return max_num                # when loop ends, biggest is the max

data = [4, 5, 6, 1, 2, 7, 8, 9]
print(find_max(data))

# Quadratic time complexity
def exp1(a, b):
  ans = 1
  while b>0:
    ans *= a
    b -= 1
  return ans

print(exp1(3, 6))

# Linear time complexity
def exp2(a, b):
  if b == 1:
    return a
  else:
    return a*exp2(a,b-1)

print(exp2(3, 6))

# Logarithm time complexity
def exp3(a, b):
  if b == 1:
    return a
  if (b%2)*2 == b:
    return exp3(a*a, b/2)
  else:
    return a*exp3(a, b-1)

print(exp3(3, 6))

# Quadratic time complexity
def g(n, m):
  x = 0
  for i in range(n):
    for j in range(m):
      x += 1
  return x

print(g(2, 10))


# Exponential time complexity






# Best complexity: O(1)
# Worst-case complexity: O(log n)
def search(s, e):
  answer = None
  i = 0
  num_of_compares = 0
  while i < len(s) and answer == None:
    num_of_compares += 1
    if e == s[i]:
      answer = True
    elif e < s[i]:
      answer = False
    i += 1
  return answer, num_of_compares

print(search([1, 2, 3, 3.5, 4, 5, 6], 4))


#


















