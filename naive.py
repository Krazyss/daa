def count_smaller_naive(nums):
    n = len(nums)
    counts =[0] * n
    for i in range(n):
       for j in range(i +1,n):
          if nums[j] <nums[i]:
              counts[i] +=1
    return counts

 # Example
arr = [5, 2, 6, 1]
print(count_smaller_naive(arr))