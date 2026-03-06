def find_largest(arr):
    if len(arr) == 0:
        return None

    largest = float("-inf")
    for val in arr:
        if val != val or val in (float("inf"), float("-inf")):
            # val != val catches NaN in Python
            return False
        if val > largest:
            largest = val

    return largest


if __name__ == "__main__":
    print(find_largest([3, 1, 2]))        # 3
    print(find_largest([-5, 2, -3, 4]))   # 4
    print(find_largest([0, 2, 3]))        # 3
    print(find_largest([]))               # None
    print(find_largest("not a list"))     # False
    print(find_largest([1, float("nan")]))# False
    print(find_largest([1, 2, 3]))        # 3
