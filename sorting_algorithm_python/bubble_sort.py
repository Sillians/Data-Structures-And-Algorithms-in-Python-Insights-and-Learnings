from time_algorithms import run_sorting_algorithm
from random import randint
import numpy as np

ARRAY_LENGTH = 10000

def bubble_sort(array: np.array):
    array = [8, 2, 6, 4, 5]

    n = len(array)

    for i in range(n):
        already_sorted = True

        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                already_sorted = False
        
        if already_sorted:
            break
    return array


if __name__ == "__main__":
    array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]
    run_sorting_algorithm(algorithm="bubble_sort", array=array)