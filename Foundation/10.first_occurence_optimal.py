def find_first_occurrence(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target and (mid == 0 or arr[mid - 1] != target):
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

arr = [2, 4, 6, 6, 6, 8, 10]
target = 6

print(find_first_occurrence(arr, target))  # Output: 2
    