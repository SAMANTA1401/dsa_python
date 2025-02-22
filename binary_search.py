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

# With each recursive call, the search space is roughly halved.
# The recursion depth is logarithmic in the size of the input array, specifically O(log(n)), 
# where n is the length of the array.


# The function uses recursive calls, which create a new stack frame for each call.
# The maximum recursion depth is O(log n), which means the space complexity is also O(log n).

result = binarySearch(arr,i,j,x)
print(result)