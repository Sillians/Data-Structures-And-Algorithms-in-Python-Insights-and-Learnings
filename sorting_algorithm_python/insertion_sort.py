import numpy as np

def insertion_sort(array: np.array) -> np.array:
    
    for i in range(1, len(array)):
        key_item = array[i]
        
        j = i - 1
        
        while j >= 0 and array[j] > key_item:
            array[j + 1] = array[j]
            j -= 1
            
        array[j + 1] = key_item
    return array

arr = [8, 2, 6, 4, 5]
print(insertion_sort(arr))