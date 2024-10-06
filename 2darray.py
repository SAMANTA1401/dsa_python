# import numpy as np

# arr=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]

# print(arr[2][3])
# print(arr.index([10,11,16,20]))
# print(len(arr))

# target_value = 20
## usign linrear Search

# for i in range(len(arr)):
#     # for j in range(4):
#     for j in range(0,4):
#         # if arr[i][j]==20:
#         #     print(i,j)
#         print(i,j)
# time complexity O(mxn)   

# arr = np.array(arr) # convert list to array 
# print("Original Array: \n", arr)

# print(arr.shape) # (3, 4)

# print(arr.shape[0])

## using binary Search as the 2d array is sorted row wise and also columns wise
## think as 1 d virtual array  of all elements arr =[1,3,5,7,10,11,16,20,23,30,34,60]
# mid=(0+(11-0))//2 = 5 ## element 11 index(1,1)
#row =mid//columns=5//4=1
#columns=mid%column=5%4=1
# m=3
# n=4

# function definition
def searchSortedMatrix(matrix,target):
    # number of rows
    m = len(matrix)
    if m == 0:
        return False
    ## number of columns 
    n =len(matrix[0])
    # Binary search implementation
    left, right = 0,m*n-1
    while left <= right:
        mid = left + (right - left)//2  #5
        # row
        mid_element = matrix[mid//n][mid%n] # 5//4, 5%3 = 1,2 >> 11
        if target == mid_element:
            print(mid//n,mid%n)
            return True
        elif target < mid_element:
            right = mid - 1
        else:
            left = mid + 1
    return False



#Driver code
matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target= 10
# print(len(matrix))
# print(len(matrix[0]))
result = searchSortedMatrix(matrix, target)
print(result)



# def arr2dSearch_binary(arr,m,n, target_value):
#     mid = (0 + (m*n-1))//2 #5

#     while mid>0:
#         r=mid//n
#         c=mid % n
#         if arr[r][c]==target_value:
#             return  [r,c]
#         elif arr[r][c] < target_value:
#             mid=(0+(mid-1))//2
#             print(mid)
#         else:
#             mid =((mid+1) + (m*n - 1))//2
#     return -1

# print(arr2dSearch_binary(arr,3,4,5))





