def binary_search(arr,target):
  left,right=0,len(arr)-1
  while left<=right:
    mid = (left+right)//2
    if arr[mid]==target:
      return mid
    elif arr[mid]>target:
      right=mid-1
    elif arr[mid]<target:
      left=mid+1
  return -1

arr=[20,40,50,80,100,134,154,221,687]
target=221
result=binary_search(arr,target)
if(result==-1):
    print(target,"is not present in ",arr)
else:
    print(target,"is present at index: ",result)