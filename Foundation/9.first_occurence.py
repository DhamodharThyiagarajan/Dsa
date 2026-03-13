def find_occurence(arr , targert):
    for i in range(len(arr)):
        if arr[i] == targert:
            return i
    return -1

arr = [2, 4, 6, 6, 6, 8, 10]
target = 6

print(find_occurence(arr, target))  # Output: 2