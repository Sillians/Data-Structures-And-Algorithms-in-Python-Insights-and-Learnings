from numpy.lib.function_base import vectorize


class Vector:
    """Represent a vector in a multidimentional space."""

    # def __init__(self, d: int):
    #     """Create d-dimensional vector of zeros"""
    #     self._coords = [0] * d

    def __init__(self, d: int):
        coords = []
        for i in range(d):
            coords.append(i**2)
        self._coords = coords

    def __len__(self):
        """Return the dimension of the vector, must be non-negative"""
        return len(self._coords)

    def __getitem__(self, j):
        """Return the jth coordinate of vector"""
        return self._coords[j]

    def __setitem__(self, key, value):
        """Set the key(th) coordinate of vector to given value"""
        self._coords[key] = value

    def __rmul__(self, factor):
        """Return the multiplication product"""
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = factor * self[j]
        return result

    def __str__(self):
        """Produce string representation of vector"""
        return '<' + str(self._coords)[1:-1] + '>'   # adapt list representation


import numpy as np
v = Vector(5)
print(v)
print(len(v))
print(3 * v)










