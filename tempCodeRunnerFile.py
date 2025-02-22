def binarySearch(arr, left, right, x):
    while left <= right:
        mid = left + (right - left) // 2
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