def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = [5, 2, 3, 1, 4, 6]
sorted_arr = bubble_sort(arr)
print("Result:", sorted_arr)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key > arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

arr = [9, 2, 8, 1, 5, 6]
sorted_arr = insertion_sort(arr)
print("Result:", sorted_arr)
