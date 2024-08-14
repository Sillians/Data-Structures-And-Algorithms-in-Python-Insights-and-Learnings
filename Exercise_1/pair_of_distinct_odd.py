"""
Write a short Python function that takes a sequence of integer values and determines if
there is a distinct pair of numbers in the sequence whose product is odd.
"""

n = [4, 5, 6, 7, 8, 9, 3, 4, 5]

def odd_pair(data):
    count = 0
    for k in range(0, len(data) - 1):
        if k % 2 != 0:
            count += 1
    return True if count >= 2 else False

# evens = [2, 4, 6, 8]
# print(odd_pair(evens))
# # print(odd_pair(n))



# Define a function named 'odd_product' that takes a list 'nums' as its argument.
def odd_product(nums):
    # Iterate through the indices of the 'nums' list using nested loops.
    for i in range(len(nums)):
        for j in range(len(nums)):
            # Check if 'i' and 'j' are different indices to avoid multiplying the same number.
            if i != j:
                # Calculate the product of elements at indices 'i' and 'j'.
                product = nums[i] * nums[j]
                # Check if the product is an odd number (using bitwise AND with 1).
                if product & 1:
                    # If an odd product is found, return True immediately.
                    return True
    # If no odd product is found, return False.
    return False

# Define three lists of integers.
dt1 = [2, 4, 6, 8]
dt2 = [1, 6, 4, 7, 8]
dt3 = [1, 3, 5, 7, 9]

# Call the 'odd_product' function for each list and print the result.
print(dt1, odd_product(dt1))
print(dt2, odd_product(dt2))
print(dt3, odd_product(dt3))



# Import the itertools module to work with combinations of numbers.
import itertools

# Define a function named 'pair_nums_odd' that takes a list 'nums' as its argument.
def pair_nums_odd(nums):
    # Create a set of unique numbers from the input list.
    uniquelist = set(nums)
    # Initialize an empty list 'result' to store pairs whose product is odd.
    result = []
    # Iterate through all distinct pairs of numbers from 'uniquelist'.
    for n in itertools.combinations(uniquelist, 2):
        # Check if the product of the pair is an odd number.
        if ((n[0] * n[1]) % 2 == 1):
            # Create a string representation of the pair.
            temp = str(n[0]) + " * " + str(n[1])
            # Append the string to the 'result' list.
            result.append(temp)
    # Return the list of distinct pairs with odd products.
    return result

# Define three lists of integers.
dt1 = [2, 4, 6, 8]
dt2 = [1, 6, 4, 7, 8]
dt3 = [1, 3, 5, 7, 9]

# Print the original sequence and the distinct pairs with odd products for each list.
print("Original sequence:")
print(dt1)
print("Distinct pair of numbers whose product is odd present in the said sequence:")
print(pair_nums_odd(dt1))

print("\nOriginal sequence:")
print(dt2)
print("Distinct pair of numbers whose product is odd present in the said sequence:")
print(pair_nums_odd(dt2))

print("\nOriginal sequence:")
print(dt3)
print("Distinct pair of numbers whose product is odd present in the said sequence:")
print(pair_nums_odd(dt3))


