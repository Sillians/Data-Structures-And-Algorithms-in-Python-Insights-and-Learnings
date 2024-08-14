# Write a short Python function, minmax(data), that takes a sequence of one or more numbers,
# and returns the smallest and largest numbers, in the form of a tuple of length two.
# Do not use the built-in functions min or max in implementing your solution.
#
# parameter = data
# data = sequence of one or more numbers
# retrun the smallest and largest numbers in tuple form of length two
# Do not use min or max functions

def minmax(data: list|tuple[int]) -> tuple:
    tuple_min_max = ()
    data.sort()

    smallest = data[0]
    largest = data[-1]
    tuple_min_max += (smallest,largest)
    return tuple_min_max
    # else:
        #     return("Invalid input")

# data = (1,2,3,4,5,6,7,8,9)
data = ['3','4','5','6','7','8','9']
print(minmax(data))



def minmax_values(data: list|tuple[int]) -> tuple:
  min_ = data[0]
  max_ = data[0]
  result = ()

  for i in range(1, len(data)):
    if data[i] > max_:
      max_ = data[i]
    else:
      data[i] < min_
      min_ = data[i]

  result += (min_, max_)
  return result



"""
R-1.3
Write a short Python function, minmax(data), that takes a sequence of
one or more numbers, and returns the smallest and largest numbers, in the
form of a tuple of length two. Do not use the built-in functions min or
max in implementing your solution.
"""


def minmax(digits):
    max = digits[0]
    min = digits[0]

    for d in digits:
        if d > max:
            max = d
        if d < min:
            min = d
    result = (min, max)

    return result

digits = input('Enter integers seperated by space: ')
digits = [int(i) for i in digits.split()] #conveting string into list of integers
print(minmax(digits))