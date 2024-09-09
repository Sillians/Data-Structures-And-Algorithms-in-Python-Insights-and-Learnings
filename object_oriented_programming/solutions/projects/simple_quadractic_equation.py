# The roots are {-b + √(b2 – 4ac)}/2a and {-b – √(b2 – 4ac)}/2a

import numpy as np

def compute_quadratic_equation(a: float, b: float, c: float):
  pm = np.array([+1, -1])
  x_numerator = ((-b) + pm * ((b**2 - (4*a*c))**(0.5)))
  x_denominator = 2*a
  x1, x2 = x_numerator / x_denominator
  return x1, x2

# 2x2 + 3x + 1 = 0
a = 2
b = 3
c = 1

print(compute_quadratic_equation(a, b, c))