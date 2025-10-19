def count_smaller(nums):
    n = len(nums)
    counts =[0] * n
    indexed_nums =list(enumerate(nums))

    def merge_sort(arr):
        if len(arr) <=1:
           return arr
        mid = len(arr) //2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        return merge(left, right)

    def merge(left, right):
       merged =[]
       i = j = right_counter =0
       while i <len(left) and j <len(right):
         if left[i][1] >right[j][1]:
           merged.append(right[j])
           right_counter +=1
           j += 1
         else:
           counts[left[i][0]] +=right_counter
           merged.append(left[i])
           i += 1
       while i <len(left):
          counts[left[i][0]] +=right_counter
          merged.append(left[i])
          i += 1
       while j <len(right):
          merged.append(right[j])
          j += 1
       return merged

    merge_sort(indexed_nums)
    return counts

#Example
arr = [5,2,6,1]
print(count_smaller(arr))