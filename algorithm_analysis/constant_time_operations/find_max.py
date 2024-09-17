def find_max(data: list) -> int:
    max_value = data[0]
    for j in data:
        if j > max_value:
           max_value = j
    return max_value

data = [4, 5, 6, 2, 3, 4]
print(find_max(data))