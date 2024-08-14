#Write a pseudo-code description of a function that reverses a list of n integers,
# so that the numbers are listed in the opposite order than they were before, and compare
# this method to an equivalent Python function for doing the same thing.



# pseudocode
# funtion(list):
#     reversed_list = []
#     for i in range(0, reversed_list_length):
#         append list[i] to reversed_list
#     return reversed_list


def reverse_list_of_integers(list):
    reversed_array=[]
    for i in range(0, len(list)):
        reversed_array.append(list[len(list)-i-1])
    return reversed_array

print(reverse_list_of_integers([1,2,3,4,5]))


# C-1.13 Write a pseudo-code description of a function that reverses a list of n
# integers, so that the numbers are listed in the opposite order than they
# were before, and compare this method to an equivalent Python function
# for doing the same thing.


def myReverse(data):
    # returning a new reversed list
    return [data[i] for i in range(len(data)-1, -1, -1)]

print(myReverse([1,2,3,4,5]))

def myReverseGen(data):
    # returning a reversed generator
    for i in range(len(data)-1, -1, -1):
        yield data[i]


def myReverseGenWithComprehension(data):
    # returning a reversed generator
    return (data[i] for i in range(len(data)-1, -1, -1))

v = myReverseGenWithComprehension([1,2,3,4,5])
print(list(v))



# Pseudo-code Description
"""
FUNCTION reverse_list(input_list):
    n = LENGTH(input_list)
    FOR i FROM 0 TO n/2 - 1:
        temp = input_list[i]
        input_list[i] = input_list[n - i - 1]
        input_list[n - i - 1] = temp
    RETURN input_list
"""

def reverse_list(input_list):
    n = len(input_list)
    for i in range(n // 2):
        temp = input_list[i]
        input_list[i] = input_list[n - i - 1]
        input_list[n - i - 1] = temp
    return input_list

# Example usage:
original_list = [1, 2, 3, 4, 5]
reversed_list = reverse_list(original_list)
print(reversed_list)  # Output: [5, 4, 3, 2, 1]


