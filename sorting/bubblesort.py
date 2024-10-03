
def bubblsort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
arrr = [5,6,9,8,4,1,3,2,7]
bubblsort(arrr)
print(arrr)