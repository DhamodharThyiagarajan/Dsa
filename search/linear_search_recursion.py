def recursive_linear_search(arr, target, start=0):
    if start >= len(arr):
        return -1  # Target value not found
    if arr[start] == target:
        return start
    return recursive_linear_search(arr, target, start + 1)


arr = [4, 7, 2, 9, 5]
target = 9

result = recursive_linear_search(arr, target)
print(result)