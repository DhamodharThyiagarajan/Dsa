def find_smallest(arr):
    if len(arr) == 0:
        return None

    smallest = float("inf")
    for val in arr:
        if  val != val or val in (float("inf"), float("-inf")):
            # val != val is a trick to catch NaN in Python
            return False
        if val < smallest:
            smallest = val

    return smallest


if __name__ == "__main__":
    print(find_smallest([3, 1, 4, 2]))   # 1
    print(find_smallest([]))             # None
    print(find_smallest("not a list"))   # False
    print(find_smallest([1, float("nan")])) # False
    print(find_smallest([10, 20, 30]))   # 10
