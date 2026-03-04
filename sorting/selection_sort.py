def selectionSort(arr):
  length = len(arr)
  for i in range(length):
    min_index=i
    for j in range(i+1,length):
      if arr[j] < arr[min_index]:
        min_index=j
    arr[i],arr[min_index]=arr[min_index],arr[i]

  print(arr)

arr=[5,4,3,2,9,8]
selectionSort(arr)