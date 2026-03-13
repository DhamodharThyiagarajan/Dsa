def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Example usage
print(factorial(5))  # Output: 120
