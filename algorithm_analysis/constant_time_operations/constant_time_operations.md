### Constant-Time Operations

Given an instance, named data, of the Python list class, a call to the function, `len(data)`, 
is evaluated in constant time. This is a very simple algorithm because the list class maintains, for each list, 
an instance variable that records the current length of the list. This allows it to immediately report that length,
rather than take time to iteratively count each of the elements in the list. Using asymptotic notation, 
we say that this function runs in `O(1)` time; that is, the running time of this function is independent of the length, `n`, 
of the list.

Another central behavior of Python’s list class is that it allows access to an arbitrary element of the 
list using syntax, `data[j]`, for integer index `j`. Because Python’s lists are implemented as array-based sequences, 
references to a list’s elements are stored in a consecutive block of memory. The `jth` element of the list can be found, 
not by iterating through the list one element at a time, but by validating the index, and using it as an offset into the 
underlying array. In turn, computer hardware supports constant-time access to an element based on its memory address. 
Therefore, we say that the expression `data[j]` is evaluated in `O(1)` time for a Python list.


### Revisiting the Problem of Finding the Maximum of a Sequence

For our next example, we revisit the `find_max` algorithm, for finding the largest value in a sequence. 
`O(n)` run-time for the `find_max` algorithm. Consistent with our earlier analysis of syntax `data[0]`, 
the initialization uses `O(1)` time. The loop executes n times, and within each iteration, 
it performs one comparison and possibly one assignment statement (as well as maintenance of the loop variable). 
Finally, we note that the mechanism for enacting a return statement in Python uses `O(1)` time. 
Combining these steps, we have that the `find_max` function runs in `O(n)` time.


### Prefix Averages

The next problem we consider is computing what are known as prefix averages of a sequence of numbers. 
Namely, given a sequence `S` consisting of `n` numbers, we want to compute a sequence `A` such 
that `A[j]` is the average of elements `S[0],...,S[j]`, for `j=0,...,n−1`. 
























































































