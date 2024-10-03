"""
Linear search 
bruth force method
time complexity is -> O(N)
no need to sort array

"""

def linear_Search(arr,item):
    for i in range(len(arr)):
        if arr[i] == item:
            return i
    return -1

a = [1,2,3,4,5,6,7,8,9]

print("the index position of element 90 is : ",linear_Search(a,90))
