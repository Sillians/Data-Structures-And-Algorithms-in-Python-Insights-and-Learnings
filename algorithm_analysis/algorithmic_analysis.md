## Algorithmic Analysis

Data structure is a systematic way of organizing and accessing data, and an algorithm is a step-by-step procedure for performing some task in a finite amount of time. 

In general, the running time of an algorithm or data structure operation increases with the input size, 
although it may also vary for different inputs of the same size. Also, the running time is affected by 
the hardware environment (e.g., the processor, clock rate, memory, disk) and software environment 
(e.g., the operating system, programming language) in which the algorithm is implemented and executed. 
All other factors being equal, the running time of the same algorithm on the same input data will be smaller
if the computer has, say, a much faster processor or if the implementation is done in a program compiled into 
native machine code instead of an interpreted implementation.

Our goal is to develop an approach to analyzing the efficiency of algorithms that:
- Allows us to evaluate the relative efficiency of any two algorithms in a way
that is independent of the hardware and software environment.
- Is performed by studying a high-level description of the algorithm without
need for implementation.
- Takes into account all possible inputs.

### Counting Primitive Operations

To analyze the running time of an algorithm without performing experiments, we perform an analysis directly on a high-level description of the algorithm (either in the form of an actual code fragment, or language-independent pseudo-code). We define a set of primitive operations such as the following:
- Assigning an identifier to an object.
- Determining the object associated with an identifier.
- Performing an arithmetic operation (for example, adding two numbers).
- Comparing two numbers.
- Accessing a single element of a Python list by index.
- Calling a function (excluding operations executed within the function).
- Returning from a function.


### Measuring Operations as a Function of Input Size
To capture the order of growth of an algorithm’s running time, we will associate, with each algorithm, 
a function `f(n)` that characterizes the number of primitive operations that are performed as a function of the input size n.

### Focusing on the Worst-Case Input
An algorithm may run faster on some inputs than it does on others of the same size. 
Worst-case analysis is much easier than average-case analysis, as it requires only the ability to 
identify the worst-case input, which is often simple. Also, this approach typically leads to better algorithms. 
Making the standard of success for an algorithm to perform well in the worst case necessarily 
requires that it will do well on every input. That is, designing for the worst case leads to stronger 
algorithmic “muscles,” much like a track star who always practices by running up an incline.

### The seven functions used in the analysis of algorithms
1. The Constant function:

The simplest function we can think of is the constant function. This is the function, `f(n) = c`, for some fixed constant c.
such as c=5, c=27, or c=210. That is, for any argument `n`, the constant function `f(n)` assigns the value c. 
In other words, it does not matter what the value of `n` is; `f(n)` will always be equal to the constant value c.

As simple as it is, the constant function is useful in algorithm analysis, because it characterizes the number 
of steps needed to do a basic operation on a computer, like adding two numbers, assigning a value to some 
variable, or comparing two numbers.


2. The Logarithm function:

One of the interesting and sometimes even surprising aspects of the analysis of data structures and algorithms is the ubiquitous presence of the logarithm function,
`f(n)` = $log{_b}{n}$, for some constant `b > 1`. This function is defined as follows: x = $log{_b}{n}$ if and only if $b^x=n$.

By definition, $log{_b}{1}$ = 0`. The value `b` is known as the base of the logarithm.

The most common base for the logarithm function in computer science is 2, as computers store integers in binary, 
and because a common operation in many algorithms is to repeatedly divide an input in half. 
In fact, this base is so common that we will typically omit it from the notation when it is 2. 
That is, for us, $log{n}$ = $log{_2}{n}$.

The following proposition describes several important identities that involve logarithms for any base greater than 1.

- Proposition(Logarithm Rules): Given real numbers a > 0, b > 1, c > 0 and d > 1, we have:

- $log{_b}{(ac)}$ = $log{_b}a$ + $log{_b}c$ 
- $log{_b}(a/c)$ = $log{_b}{a}$ − $log{_b}{c}$ 
- $log{_b}a^{c}$ = $clog{_b}{a}$
- $log{_b} a$ = $log{_d}{a}$ / $log{_d}{b}$
- $b^{log{_d}{a}}$ = $a^{log{_d}{b}}$


3. The Linear function:

Another simple yet important function is the linear function, `f(n) = n.`
That is, given an input value `n`, the linear function `f` assigns the value `n` itself. This function arises in algorithm analysis any time we have to do a single basic operation for each of n elements.


4. The N-Log N function:

The n-log-n function, given as; `f(n) = nlogn`. that is, the function that assigns to an input `n` the value of `n` times the logarithm base-two of `n`. 
This function grows a little more rapidly than the linear function and a lot less rapidly than the quadratic function;
therefore, we would greatly prefer an algorithm with a running time that is proportional to `nlogn`, 
than one with quadratic running time. 


5. The Quadratic function:

Another function that appears often in algorithm analysis is the quadratic function, `f(n)` = n^{2}. 
That is, given an input value `n`, the function `f` assigns the product of `n` with itself (in other words, “n squared”).

The main reason why the quadratic function appears in the analysis of algorithms is that there are many algorithms 
that have nested loops, where the inner loop performs a linear number of operations and the outer loop is performed 
a linear number of times. Thus, in such cases, the algorithm performs n·n = n^{2} operations.


6. The Cubic function and other Polynomials:

The cubic function, `f(n)` = n^{3}, which assigns to an input value n the product of n with itself three times. 
This func- tion appears less frequently in the context of algorithm analysis than the constant, linear, 
and quadratic functions previously mentioned, but it does appear from time to time.

- Polynomials

Most of the functions we have listed so far can each be viewed as being part of a larger class of functions, the `polynomials`. 
A polynomial function has the form, `f(n)` = $a{_0}$ + $a{_1}n$ + $a{_2}n^{2}$ + $a{_3}n^{3}$ +···+ $a{_d}n^{d}$. 

where $a{_0}$, $a{_1}$ , . . . , $a{_d}$ are constants, called the coefficients of the polynomial, 
and $a{_d}$ != 0. Integer `d`, which indicates the highest power in the polynomial, is called the degree of the polynomial.

Running times that are polynomials with small degree are generally better than polynomial running times with larger degree.


7. The Exponential function:

Another function used in the analysis of algorithms is the exponential function, `f(n)` = $b^{n}$. 
where b is a positive constant, called the `base`, and the argument `n` is the `exponent`. 
That is, function `f(n)` assigns to the input argument `n` the value obtained by multiplying the base `b` by itself `n` times. 
As was the case with the logarithm function, the most common base for the exponential function in algorithm analysis is `b=2`. 





































































