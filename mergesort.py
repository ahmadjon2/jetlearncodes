def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left_half = mergesort(arr[:mid])
    right_half = mergesort(arr[mid:]) 
    return merge(left_half,right_half)

def merge(left,right):
    sort_arr = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            sort_arr.append(left[i])
            i += 1
        else :
            sort_arr.append(right[j])
            j += 1
    sort_arr.extend(left[i:])
    sort_arr.extend(right[j:])  
    return sort_arr

arr = [8,2,7,6,3,4,5,1,]
sort_arr = mergesort(arr)
print(sort_arr)