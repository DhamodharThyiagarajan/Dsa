def merge_overlapping_intervals(arr):
    n = len(arr)
    
    # Sort the intervals based on the start time
    arr.sort(key=lambda x: x[0])
    
    ans = [arr[0]]
    
    for i in range(1, n):
        last = ans[-1]
        curr = arr[i]
        
        # If current interval overlaps with the last one in ans
        if curr[0] <= last[1]:
            last[1] = max(last[1], curr[1])
        else:
            ans.append(curr)
    
    return ans

# Example usage
arr = [[1, 3], [8, 10], [2, 6], [15, 18]]
ans = merge_overlapping_intervals(arr)
print("The merged intervals are:")
for interval in ans:
    print(f"[{interval[0]}, {interval[1]}]")  # Output: [1, 6], [8, 10], [15, 18]