import numpy as np

def merge(left: np.array, right: np.array) -> np.array:
    
    if len(left) == 0:
        return right
    
    if len(right) == 0:
        return left
    
    result_array = []
    left_index = right_index = 0
    
    while len(result_array) < len(left) + len(right):
        if left[left_index] <= right[right_index]:
            result_array.append(left[left_index])
            left_index += 1
        
        else:
            result_array.append(right[right_index])
            right_index += 1
            
        if right_index == len(right):
            result_array += left[left_index:]
            break
        
        if left_index == len(left):
            result_array += right[right_index:]
            break

    return result_array


def merge_sort(array: np.array) -> np.array:
    if len(array) < 2:
        return array
    
    midpoint = len(array) // 2
    
    merged_array = merge(left=merge_sort(array[:midpoint]), right=merge_sort(array[midpoint:]))
    return merged_array


arr = [2, 5, 8, 3, 7, 5, 4]
print(merge_sort(array=arr))