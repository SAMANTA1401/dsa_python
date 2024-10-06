# Recurrence Relation             ## T(n) = 1 when n=1
# T(n) = T(n/3) +c                ## T(n) = T(n/3) +c when n>1
# T(n) = T(n/3^2) + 2c
# T(n) = T(n/3^k) +kc >> T(n) = 1 + log_3(n).c >> O(log_3(n)) --Time complexity
# n/3^k = 1
# n = 3^k
# k = log_3(n)

##function definition
def ternarySearch(l,r,x,arr):
    while l<= r:
        mid1 = l +(r-l)//3 #3
        mid2 = r - (r-l)//3 #6

        if x == arr[mid1]:
            return mid1
        elif x == arr[mid2]:
            return mid2
        ## first search space
        elif x< arr[mid1]:
            return ternarySearch(l,mid1-1,x,arr)
        ## third search space
        elif x > arr[mid2]:
            return  ternarySearch(mid2+1,r,x,arr)
        ## second search space
        else:
            return ternarySearch(mid1+1, mid2-1, x, arr)
    return -1





##Driver Code
arr = [1,2,3,4,5,6,7,8,9,10]
l =0
r=len(arr) - 1
x = 8
## function calling
result = ternarySearch(l,r,x,arr)
print("The element is present at index", result)