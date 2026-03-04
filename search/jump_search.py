#jump search
import math
def jump_search(arr, target):
    n = len(arr) #n = 8
    step = int(math.sqrt(n)) #step = √8 ≈ 2
    prev = 0
    if arr[prev] == target: #arr[prev] = 1 ==0
      return prev
    if arr[min(step,n)-1] == target:
      return min(step, n) - 1
    while prev < n and arr[min(step, n) - 1] < target: #arr[min(2, 8)-1] = arr[1] = 3
      prev=step #prev = 2
      step+=int(math.sqrt(n)) #step=4
      if prev >= n: #2>=8
        return -1
      for i in range(prev, min(step, n)):  #After jumping: prev = 4, step = 6
        if arr[i] == target:  # i=4 , i=5  arr[4]=0  arr[5]=11
          return i   # return 5
    return -1

arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = 11
result = jump_search(arr, target)
print(result)  # Output: 5