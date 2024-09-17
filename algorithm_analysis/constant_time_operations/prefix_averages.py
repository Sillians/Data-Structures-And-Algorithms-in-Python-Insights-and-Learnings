def prefix_average(arr: list, j: int) -> float:
    n = len(arr)
    prefix_avg = []
    total_sum = 0

    for i in range(n):
        total_sum += arr[i]
        avg = total_sum / (i + 1)
        prefix_avg.append(avg)

    return prefix_avg[j]

arr = [2, 4, 6, 8, 5]
print(prefix_average(arr, 0))