"""

def binary_Search(arr,item):
    left =0
    right = len(arr)-1

    # mid = (left+right)/2
    while left<=right:
        mid = (left+right)//2
        if arr[mid]> item:
            right = mid -1
        elif arr[mid]<item:
            left = mid +1
        elif arr[mid] == item:
            return mid
        
    return -1

    """
# binary search with recursion 
def binary_Search(arr,ele,left,right):
    if left<=right:
        mid = (left+right)//2
        if arr[mid] == ele:
            return mid
        elif arr[mid]> ele:
            return binary_Search(arr,ele,left, mid-1)
        else:
            return binary_Search(arr,ele,mid+1, right)
            
    else :
        return -1

# [10,20,30,40,50,60,70,80,90,100]

arr = [10,20,30,40,50,60,70,80,90,100]
ele = 50
# print(f'the index of element of {ele} is : ', binary_Search(arr,ele))
print(f'the index of element of {ele} is : ', binary_Search(arr,ele,0,len(arr)-1))
