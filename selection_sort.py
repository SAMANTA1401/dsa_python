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
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index = j
         #swap of the element at i and min index
        arr[i], arr[min_index] = arr[min_index],arr[i]
    return arr


arr = [50,38,45,79,19,27,29]
result = selectionSort(arr)
print(result)

#time complexity is O(n^2)