arr = [50,38,45,79,19,27,29]
#38,50 , 45,79,19,27,29
#38,45,50,79,19,27,29


#time complexity=O(n^2) descending order
#if ascending order best case then time complexity=O(n) as swaps almost zero
# explain insertion sort 

#using for loop
# def insertionSort(arr):
#     for i in range(1,len(arr)):
#         for j in range(i, 0, -1):
#             if arr[j] <arr[j-1] :
#                 arr[j], arr[j-1] = arr[j-1], arr[j]
#             else:
#                 break # # Stop if no swap needed
#     return arr

# print(insertionSort(arr))

# Optimization
# Uses a "key" value to avoid multiple swaps.
# Shifts elements instead of swapping repeatedly.

#using while loop
arr = [50,38,45,79,19,27,29]

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]  # Store the current element to insert
        j = i - 1     # Start from the last element of sorted portion
        while j >= 0 and arr[j] > key:  # Shift elements greater than key
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key  # Place key in its correct position
    return arr

# Test
arr = [5, 2, 9, 1, 5, 6]
print(insertionSort(arr))  # Output: [1, 2, 5, 5, 6, 9]

# Outer Loop: i iterates over the array starting at index 1.
# Key: arr[i] is the element to insert into the sorted portion (arr[0:i]).
# Inner Loop:
# while j >= 0 and arr[j] > key: Shifts elements right if they’re greater than key.
# Once the condition fails, j + 1 is the correct position for key.
# Example: [5, 2, 9, 1, 5, 6]
# i=1: key=2, shift 5 right → [2, 5, 9, 1, 5, 6].
# i=2: key=9, no shifts → [2, 5, 9, 1, 5, 6].
# i=3: key=1, shift 9, 5, 2 right → [1, 2, 5, 9, 5, 6].
# i=4: key=5, shift 9 right → [1, 2, 5, 5, 9, 6].
# i=5: key=6, shift 9 right → [1, 2, 5, 5, 6, 9].

