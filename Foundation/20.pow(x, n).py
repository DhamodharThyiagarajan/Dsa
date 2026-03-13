def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n - 1)

print(power(2, 4))  # Output: 16      2 * power(2, 3)

                                    # 2 * (2 * power(2, 2))

                                    # 2 * (2 * (2 * power(2, 1)))

                                    # 2 * (2 * (2 * (2 * power(2, 0))))




