import numpy as np
def create_polynomial_design_matrix(x, degree):
    # Initialize an empty design matrix
    X = np.ones((len(x), 1))

    # Append higher-order polynomial features
    for i in range(1, degree + 1):
        X = np.column_stack((X, x ** i))

    return X

# Example input data (x values)
x = np.array([1, 2, 3, 4, 5])

# Desired degree of polynomial
degree = 3

# Create polynomial design matrix
X = create_polynomial_design_matrix(x, degree)

print("Design Matrix:")
print(X)
