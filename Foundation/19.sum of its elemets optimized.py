def sum_array(arr, index=0):
    if index == len(arr):
        return 0
    return arr[index] + sum_array(arr, index + 1)

# Example usage
print(sum_array([1, 2, 3, 4, 5]))  # Output: 15