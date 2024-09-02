#The Vector class of Section 2.3.3 provides a constructor that takes an integer d, and produces a d-dimensional vector
# with all coordinates equal to 0. Another convenient form for creating a new vector would be to send the constructor a
# parameter that is some iterable type representing a sequence of numbers, and to create a vector with dimension
# equal to the length of that sequence and coordinates equal to the sequence values. For example, Vector([4, 7, 5])
# would produce a three-dimensional vector with coordinates <4, 7, 5>. Modify the constructor so that either of these
# forms is acceptable; that is, if a single integer is sent, it produces a vector of that dimension with all zeros, but
# if a sequence of numbers is provided, it produces a vector with coordinates based on that sequence.


from typing import List

class Vector:
    """Represent a vector in a multidimentional space."""

    def __init__(self, dim_no: List[int]):
        """Create d-dimensional vector of zeros"""
        if isinstance(dim_no, int):
            self._coords = [0] * dim_no
        elif isinstance(dim_no, list):
            self._coords = dim_no
        else:
            raise ValueError("Input Sequence must be dimension in int or list")

    def __len__(self):
        """Return the dimension of the vector, must be non-negative"""
        return len(self._coords)

    def __getitem__(self, j):
        """Return the jth coordinate of vector"""
        return self._coords[j]

    def __setitem__(self, key, value):
        """Set the key(th) coordinate of vector to given value"""
        self._coords[key] = value

    def __str__(self):
        """Produce string representation of vector"""
        return '<' + str(self._coords)[1:-1] + '>'   # adapt list representation


import numpy as np
v = Vector([5, 4, 5, 2])
print(v)
print(len(v))