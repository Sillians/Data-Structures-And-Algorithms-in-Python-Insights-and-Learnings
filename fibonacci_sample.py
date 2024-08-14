from __future__ import print_function
import sys

a = 0
b = 1
try:
    n = int(input('How many fibonacci numbers do you want : '))
except ValueError:
    print("Integer value expected. Exiting.")
    sys.exit(2)
if n < 0:
    print('Positive Integer expected. Exiting.')
    sys.exit(2)

if n == 0:
    print(None, end=' ')
elif n == 1:
    print(a, end=' ')
elif n == 2:
    print(a, end=' ')
    print(b, end=' ')
else:
    for i in range(n - 2):
        if i == 0:
            print(a, end=' ')
            print(b, end=' ')
        c = a + b
        a = b
        b = c
        print(c, end=' ')
