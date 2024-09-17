Our final algorithm, `prefix_averages3`, Just as with our first two algorithms, 
we are interested in computing, for each `j`, the prefix `sum S[0] + S[1] + · · · + S[ j]`, 
denoted as `total` in our code, so that we can then compute the prefix average `A[j] = total / (j + 1)`. 
However, there is a key difference that results in much greater efficiency.

The analysis of the running time of algorithm prefix average3 follows:
- Initializing variables `n` and total uses `O(1)` time.
- Initializing the list A uses `O(n)` time.
- There is a single for loop, which is controlled by counter `j`. The maintenance
of that counter by the range iterator contributes a total of `O(n)` time.
- The body of the loop is executed `n` times, for `j=0,...,n−1`. Thus, statements `total += S[j]` and `A[j] = total / (j+1)` 
are executed `n` times each. Since each of these statements uses `O(1)` time per iteration, 
their overall contribution is `O(n)` time.


The running time of algorithm `prefix_average3` is given by the sum of the four terms. 
The first is `O(1)` and the remaining three are `O(n)`. By a simple application, the running time 
of `prefix_average3` is `O(n)`, which is much better than the quadratic time of 
algorithms `prefix_average1` and `prefix_average2`.

