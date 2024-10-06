## search for an element 15 and if it's present in an array , return the index of that element 
##suppose the searching element is not present in an array, rerurn -1
## time complexitty O(n)
## space complexitty : O(1)
## function definition

def linearSearch(arr, x):
    for i in range (len(arr)):
        if arr[i] == x:
            return i
    return -1

## Driver code
arr = [3,4,2,5,68,3,6]  ## time complexity worst case O(n) best case O(1) average case  O(n/2)=>O(n)/2=O(n)
x = 8                   ## space complexity  O(1)=constant
#function calling
result = linearSearch(arr, x)
print(result)