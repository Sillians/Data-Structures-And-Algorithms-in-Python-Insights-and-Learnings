"""
Demonstrate how to use Python’s list comprehension
syntax to produce the list [1, 2, 4, 8, 16, 32, 64, 128, 256].
"""

# Method 1
lst = []
for i in range(9):
    lst.append(2**i)

print(lst)

# Method 2
lst_ = [2**i for i in range(9)]
print(lst_)

# Method 3
lst = [1]
n = 0

while n <= 7:
  x = lst[-1] * 2
  lst.append(x)
  n+=1


"""
1.9 What parameters should be sent to the range constructor, to produce a
range with values 50, 60, 70, 80?
"""

lst = [n for n in range(50, 81, 10)]
print(lst)


"""
1.10 What parameters should be sent to the range constructor, to produce a
range with values 8, 6, 4, 2, 0, −2, −4, −6, −8
"""

lst = [n for n in range(-8, 9, 2)]
print(lst)