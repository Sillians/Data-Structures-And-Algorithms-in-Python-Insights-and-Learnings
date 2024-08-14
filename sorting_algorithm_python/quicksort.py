import numpy as np
from random import randint

def quicksort(array: np.array) -> np.array:
    if len(array) < 2:
        return array
    
    low, same, high = [], [], []
    
    rand = randint(0, len(array))
    
    pivot = array[rand]
    for item in array:
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        else:
            high.append(item)
    
    return (quicksort(low) + same + quicksort(high))

array = [2, 5, 8, 3, 7, 5, 4] 
print(quicksort(array))