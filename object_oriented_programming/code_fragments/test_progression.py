from progression import Progression
from arithmetic_progression import ArithmeticProgression
from geometric_progression import GeometricProgression
from fibonacci_progression import FibonacciProgression


if __name__ == "__main__":
    print('Default Progression')
    Progression().make_progression(20)

    print("Arithmetic progression with increment 5: ")
    ArithmeticProgression(5).make_progression(10)

    print('Arithmetic progression with increment 5 and start 2: ')
    ArithmeticProgression(5, 2).make_progression(20)

    print('Geometric progression with default base:')
    GeometricProgression().make_progression(15)

    print('Geometric progression with base 3:')
    GeometricProgression(3).make_progression(15)

    print('Fibonacci progression with default start values:')
    FibonacciProgression().make_progression(6)

    print('Fibonacci progression with start values 3 and 4:')
    FibonacciProgression(3,4).make_progression(10)