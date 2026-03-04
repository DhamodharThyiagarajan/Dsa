def insertion_sort(arr):
  lenght=len(arr)

  for i in range(1,length):
    key=arr[i]
    j=i-1
    while(j>=0 and key<arr[j]):
      arr[j+1]=arr[j]
      j-=1
    arr[j+1]=key
  print(arr)

arr=[8,6,5,4,7]
insertion_sort(arr)