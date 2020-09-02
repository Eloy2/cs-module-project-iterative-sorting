def linear_search(arr, target):
    for i in arr:
        if i == target:
            return arr.index(i)

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    start = 0
    end = len(arr) - 1

    while start <= end:
        middle = (start + end) // 2
        mid_value = arr[middle]
        if mid_value == target:
            return middle
        if mid_value > target:
            end = middle - 1
        else:
            start = middle + 1

    return -1  # not found
