"""
ExerciseR-2.12 uses the __mul__ method to support multiplying a Vector by a number,
while Exercise R-2.14 uses the __mul__ method to support computing a dot product of two vectors.
Give a single implementation of Vector. __mul__ that uses run-time type checking to support both syntaxes
u * v and u * k, where u and v designate vector instances and k represents a number.
"""

from typing import Sequence, Optional, Mapping
import numpy as np

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

    def __mul__(self, other: Optional[Mapping[int, float]]):
        if type(other) == int or type(other) == float:
            product_mul = Vector(len(self))
            for j in range(len(self)):
                product_mul[j] = self[j]*other
            return product_mul
        else:
            if len(self) != len(other):
                raise ValueError('Both dimensions of the vectors must be of same length')
            result = 0
            for j in range(len(self)):
                result += self[j] * other[j]
            return result

    def __str__(self):
        """Produce string representation of vector"""
        return '<' + str(self._coords)[1:-1] + '>'   # adapt list representation





v = Vector(5)
print(v)

u = [0, 20, 30, 40, 60]
vtr = np.array(u)
mul_ = v * vtr
print(mul_)

k = 7
mul__ = v * k
print(mul__)










