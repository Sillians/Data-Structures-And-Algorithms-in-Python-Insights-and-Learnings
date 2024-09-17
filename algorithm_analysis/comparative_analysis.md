### Comparative Analysis

Suppose two algorithms solving the same problem are available: an `algorithm A`, which has a running time of `O(n)`, 
and an `algorithm B`, which has a running time of $O(n^{2})$. Which algorithm is better? We know that `n` is $O(n^{2})$, 
which implies that `algorithm A` is asymptotically better than `algorithm B`, although for a small value of `n`, 
`B` may have a lower running time than `A`.

We can use the `big-Oh notation` to order classes of functions by asymptotic growth rate. 
Our seven functions are ordered by increasing growth rate in the following sequence, that is, if a function 
`f(n)` precedes a function `g(n)` in the sequence, then `f(n)` is `O(g(n))`:

1, logn, n, nlogn, $n^{2}$, $n^{3}$, $2^{n}$.

illustration of the growth rates of the seven functions. 

| n   | logn  | n   | nlogn | $n^{2}$ | $n^{3}$     | $2^{n}$           |
|-----|-------|-----|-------|---------|-------------|-------------------|     
| 8   | 3     | 8   | 24    | 64      | 512         | 256               |
| 16  | 4     | 16  | 64    | 256     | 4,096       | 65,536            |
| 32  | 5     | 32  | 160   | 1,024   | 32,768      | 4,294,967,296     |
| 64  | 6     | 64  | 384   | 4,096   | 262,144     | 1.84 × $10^{19}$  |
| 128 | 7     | 128 | 896   | 16,384  | 2,097,152   | 3.40 × $10^{38}$  |
| 256 | 8     | 256 | 2,048 | 65,536  | 16,777,216  | 1.15 × $10^{77}$  |
| 512 | 9     | 512 | 4,608 | 262,144 | 134,217,728 | 1.34 × $10^{154}$ |

Selected values of fundamental functions in algorithm analysis. 


### Some Words of Caution

A few words of caution about asymptotic notation are in order at this point. First, note that the use of the 
big-Oh and related notations can be somewhat misleading should the constant factors they “hide” be very large. 
For example, while it is true that the function $10^{100}n$ is `O(n)`, if this is the running time of an 
algorithm being compared to one whose running time is `10nlogn`, we should prefer the `O(nlogn)`-time algorithm, 
even though the linear-time algorithm is asymptotically faster. This preference is because the constant factor, 
$10^{100}$, which is called “one googol,” is believed by many astronomers to be an upper bound on the number 
of atoms in the observable universe. So we are unlikely to ever have a real-world problem that has this number 
as its input size. Thus, even when using the `big-Oh notation`, we should at least be somewhat mindful of the 
constant factors and lower-order terms we are “hiding.”

The observation above raises the issue of what constitutes a “fast” algorithm. Generally speaking, 
any algorithm running in `O(nlogn)` time (with a reasonable constant factor) should be considered efficient. 
Even an $O(n^{2})$-time function may be fast enough in some contexts, that is, when `n` is small. 
But an algorithm running in $O(2^{n})$ time should almost never be considered efficient.

### Exponential Running Times

If we must draw a line between efficient and inefficient algorithms, therefore, it is natural to make this 
distinction be that between those algorithms running in polynomial time and those running in exponential time.
That is, make the distinction between algorithms with a running time that is `O(nc)`, for some constant `c > 1`, 
and those with a running time that is `O(bn)`, for some constant `b > 1`. 

This too should be taken with a “grain of salt,” for an algorithm running in $O(n^{100})$ time should 
probably not be considered “efficient.” Even so, the distinction between polynomial-time and exponential-time 
algorithms is considered a robust measure of tractability.
































































