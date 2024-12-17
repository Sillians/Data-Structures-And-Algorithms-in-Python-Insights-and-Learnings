def binary_search(data: list, target: int, low: float, high: float) -> int:
    """Return True if target is found in indicated portion of a Python list

       The search only considers the portion from data[low] to data[high] inclusive.
    """

    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            # recur on the portion left of the middle
            return binary_search(data, target, low, mid - 1)
        else:
            # recur on the portion right of the middle
            return binary_search(data, target, mid + 1, high)


data = [2, 4, 5, 7, 8, 12, 14, 17, 19, 22, 25, 27, 28, 33, 37]
n = len(data)
low = 0
high = n - 1

# Time complexity: O(log n)
print(binary_search(data, 22, low, high))