# arr = [50,38,45,79,19,27,29]

# min = at index 0 ie 50 compare with another  number in the array. If it is 
# smaller then replace that number with min and move to next element

# pass1 >> 
# arr=[19,(38,45,79,27,29,50)] #one swap
#pass 2
# arr =[19,27,(45,79,38,29,50)] #one swap

# [19,27,29,(79,38,45,50)] #One more swap
# arr =[19,27,29,38,(97,50)]. 

##total 7 swaps

##function definition
def selectionSort(arr):
    n = len(arr)
    if n <= 1:  # Early return for empty or single-element array
        return arr
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap only if a smaller element was found
        if min_index != i:
            #swap of the element at i and min index
            arr[i], arr[min_index] = arr[min_index],arr[i]
    return arr

# Time Complexity
# Worst Case: O(n²) – compares every pair in the unsorted portion (e.g., reverse sorted array).
# Best Case: O(n²) – still performs all comparisons, even if already sorted (unlike insertion sort).
# Average Case: O(n²).
# The optimization doesn’t affect asymptotic complexity but reduces constant factors (fewer swaps).
# Space Complexity
# O(1) – in-place sorting, only uses a few variables (n, i, j, min_index).



arr = [50,38,45,79,19,27,29]
result = selectionSort(arr)
print(result)

#time complexity is O(n^2)