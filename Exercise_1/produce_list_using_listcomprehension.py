# My rough method
list_ = []
for k in range(0, 10+1):
  list_.append(k)

new_list_ = [0]
for j in range(1, len(list_) - 1):
  n = new_list_[-1] + j
  new_list_.append(n)

print([2*i for i in new_list_])


# #Demonstrate how to use Python’s list comprehension syntax to produce the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90].

def progression():
    return list(x*(x+1) for x in range(0,10))

print(progression())