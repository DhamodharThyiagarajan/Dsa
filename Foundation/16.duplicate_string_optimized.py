def remove_duplicates(arr):
    return list(dict.fromkeys(arr))  # Preserves order while removing duplicates

arr = [1, 2, 3, 2, 4, 1, 5]
print(remove_duplicates(arr))  # Output: [1, 2, 3, 4, 5]
