mylist = [3,1,2,5,4]
for i in range(0,len(mylist)):
    for g in range(i,len(mylist)):
        if mylist[i] < mylist[g]:
            mylist[i],mylist[g] = mylist[g],mylist[i]
print(mylist)

def insertion_sort(arr):
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
list123 = [9,8,2,4,5,6,1,3,7,10]
insertion_sort(list123)
print(list123)