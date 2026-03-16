def sorted_squares(nums):
    result = []
    for num in nums:
        result.append(num * num)
    result.sort()
    return result

# Example usage
print(sorted_squares([-4, -2, 0, 2, 4]))         # Output: [0, 4, 4, 16, 16]
print(sorted_squares([-5, -3, -1, 0, 2, 4, 6]))  # Output: [0, 1, 4, 9, 16, 25, 36]