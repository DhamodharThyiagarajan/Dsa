def sorted_squares(nums):
    result = [0] * len(nums) #[0, 0, 0, 0, 0]
    left = 0
    right = len(nums) - 1
    index = right

    while left <= right:
        left_square = nums[left] ** 2
        right_square = nums[right] ** 2

        if left_square > right_square:
            result[index] = left_square
            left += 1
        else:
            result[index] = right_square
            right -= 1

        index -= 1

    return result

# Example usage
print(sorted_squares([-4, -2, 0, 2, 4]))# Output: [0, 4, 4, 16, 16]
print(sorted_squares([-5, -3, -1, 0, 2, 4, 6])) # Output: [0, 1, 4, 9, 16, 25, 36]
