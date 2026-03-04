def bubbleSort(arr):
  length =len(arr)
  for i in range (length):
    for j in range(0, length-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
  print(arr)


arr=[7,2,8,4,3,5]
bubbleSort(arr)