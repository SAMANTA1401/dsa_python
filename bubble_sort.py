##1. buble sort descending order
## 7,5,1,2,3
##(7523)1  i=0  j=0-3 > four iteration 4 gap  5-i-1
##(753)21   i=1 j=1 -4  > three gap 3 iteration 5-i-1


#  comparison based >> (n-1)+(n-2)+(n-3)+(n-4)......3+2+1 = n(n-1)/2  =(n-1)(n-1+1)/2 O(n*2) >> bubble sort 
## swaps >> n(n-1)/2 => O(n^2)

## not using any extra spacces >> space complexity O(1)

lst = [5,1,7,2,3]

for i in range(len(lst)): # n times
    for  j in range(len(lst)-i-1):  # (n-1) times
        if lst[j] < lst[j+1]:
            temp = lst[j]
            lst[j]= lst[j+1]
            lst[j+1] = temp
#time constant=n*(n-1)*c=O(n^2). space constant is O(1) as it uses only a single additional memory (temp) to swap the element
print(lst)

##2. buble sort ascending order

for i in range(len(lst)):
    for  j in range(len(lst)-i-1):
        if lst[j] > lst[j+1]:
            temp = lst[j]
            lst[j]= lst[j+1]
            lst[j+1] = temp

print(lst)


##method definition
def bubblesort(arr):
    for i in range(len(arr)):
        for  j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                # temp = arr[j]
                # arr[j]= arr[j+1]
                # arr[j+1] = temp
    return arr




#driver code
##3. find the no of element not in ascending order
arr = [1,2,6,3,1,4]
result = bubblesort(arr)
print(result)






