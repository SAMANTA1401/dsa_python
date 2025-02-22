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
        mid = (i+(j-1))//2 # subtract 0 or 1
        print(mid)
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            i = mid+1
        else:
            j = mid-1
    return -1


## Driver code
## Sorted array
arr = [2,5,10,14,18,22,27,35,40,56]
x = 35
i=0 # first index 
j = len(arr)-1 # 8 last index
print(j)

# With each recursive call, the search space is roughly halved.
# The recursion depth is logarithmic in the size of the input array, specifically O(log(n)), 
# where n is the length of the array.


# The function uses recursive calls, which create a new stack frame for each call.
# The maximum recursion depth is O(log n), which means the space complexity is also O(log n).

result = binarySearch(arr,i,j,x)
print(result)

# This is a more modern and safer way to calculate the middle index. 
# It avoids potential integer overflow issues when left and right are large.
def binarySearch(arr, left, right, x):
    while left <= right:
        # first divide then add
        mid = left + (right - left) // 2  # mid = (i+(j-1))//2 (older way) first add then divide
        print(mid)
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1

## Driver code
## Sorted array
arr = [2, 5, 10, 14, 18, 22, 27, 35, 40, 56]
x = 35
left = 0  # first index
right = len(arr) - 1  # last index
print(right)
result = binarySearch(arr, left, right, x)
print("Element found at index", result)