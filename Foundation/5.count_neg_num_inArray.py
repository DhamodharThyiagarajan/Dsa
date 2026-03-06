def count_negative_numbers(arr):
   count = 0
   for num in arr:
       if num < 0:
           count += 1
   return count

arr = [10, -2, 5, -20, 1, 50, 60, -50, -12, -9]
print("Total negative elements:", count_negative_numbers(arr))