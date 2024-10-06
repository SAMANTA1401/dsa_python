## Divide and cconquer
## array should be sorted
## reccurtion calling the function inside the method  itself  with different set of parameter
## time complexity T(n) = logn base 2
## recursion relation

def binarySearch(arr,i,j,x):
    while i <= j:
        mid = (i+(j-1))//2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            return binarySearch(arr,mid+1,j,x)
        else:
            return binarySearch(arr,i,mid - 1,x)
    ## searching element is not present in the array
    return -1

# or 
def binarySearch(arr,i,j, x):
    while i<=j:
        mid = (i+(j-1))//2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            i = mid+1
        else:
            j = mid-1
    return -1

## Driver code
## Sorted array
arr = [2,5,10,14,18,22,27,35,40,59]
x = 4
i=0
j = len(arr)-1

result = binarySearch(arr,i,j,x)
print(result)