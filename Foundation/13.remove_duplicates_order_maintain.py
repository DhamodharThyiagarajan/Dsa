def remove_duplicates(arr):
    unique_arr = []
    for item in arr:
        if item not in unique_arr:
            unique_arr.append(item)
    return unique_arr

arr = [1, 2, 3, 2, 4, 1, 5]
print(remove_duplicates(arr))  # Output: [1, 2, 3, 4, 5]
