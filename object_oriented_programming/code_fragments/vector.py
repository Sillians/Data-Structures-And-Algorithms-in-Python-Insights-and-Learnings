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

    def __add__(self, other):
        """Return the sum of two vectors"""
        if len(self) != len(other):    # relies on __len__ method
            raise ValueError('dimensions must agree')
        result = Vector(len(self))     # start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __sub__(self, other):
        """Return the subtracted values of the two vectors"""
        if len(self) != len(other):
            raise ValueError('Both dimensions must be of same length')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result

    def __eq__(self, other):
        """Return True if vector has same coordinates as other."""
        return self._coords == other

    def __ne__(self, other):
        """Return True if vector differs from other."""
        return self._coords != other                   # rely on existing _-eq__ definition

    def __str__(self):
        """Produce string representation of vector"""
        return '<' + str(self._coords)[1:-1] + '>'   # adapt list representation

    def __pow__(self,b):
        result = [value**b for value in self._coords]
        return result


import numpy as np
v = Vector(5)
print(v)
print(len(v))

u = [0, 20, 30, 40, 60]
vtr = np.array(u)
new_add = v + vtr
new_sub = v - vtr
print(new_add)
print(new_sub)
print(v == vtr)
print(v != vtr)
print(v ** 2)









