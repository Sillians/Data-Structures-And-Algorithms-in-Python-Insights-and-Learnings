def find_max(data: list) -> int:
    max_value = data[0]   # O(1) time
    for j in data:        # executes 'n' times
        if j > max_value:
           max_value = j
    return max_value      # O(1) time

data = [4, 5, 6, 2, 3, 4]
print(find_max(data))    # Runs in O(n) time