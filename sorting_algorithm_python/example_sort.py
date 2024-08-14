from time_algorithms import run_sorting_algorithm
from random import randint

ARRAY_LENGTH = 10000

if __name__ == "__main__":
    array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]
    
    run_sorting_algorithm(algorithm="sorted", array=array)