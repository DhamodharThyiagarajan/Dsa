def power(x, n):
    if n == 0:
        return 1

    if n % 2 == 0:
        temp = power(x, n // 2)
        return temp * temp

    return x * power(x, n - 1)

# Example usage
print(power(2, 4))  # Output: 16     
                                    # (2 * power(2, 2))

                                    # (2 * (2 * power(2, 1)))

                                    #  (2 * (2 * (2 * power(2, 0))))

                                    # (2 * (2 * (2 * (2 * 1)))) =16