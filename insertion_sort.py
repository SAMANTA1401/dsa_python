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
#     return arr

# print(insertionSort(arr))

#using while loop
arr = [50,38,45,79,19,27,29]

def insertionSort(arr):
    for i in range(1,len(arr)):
        j = i-1
        key = arr[i]
        while j>=0 and key<arr[j]:
            arr[j+1] =arr[j]
            j -= 1
        # arr[j+1] = key  #arr[i]
    return arr

print(insertionSort(arr))



# for i in range(1,len(arr)):
#     print(i)
#     print('****************')
#     for j in range(i,0,-1):
#         print(j)
#         print('################################')

                