# complete binary tree >> heap base datastructure
# condtion:
# 1. first complete initial level then move to next level
# 2. first complete left child node then move to right child node

# almost complete binary tree one leaf Node    Very less watage of space

# n = number of nodes
# k = number of level

# n = 2^k -1 (complete binary tree)
# k = log_2(n+1)
# n=63
# k = log_2(64)
# k = log_2 2^6
# k = 6* log_2 2

# n/2 = number of leaf nodes
# n/2 = number of non leaf nodes

# left node index = 2*i + 1

# right node index = 2*i + 2


# Heap 
# 1. min heap >> parent  node < child node   >> root node least element
# 2. max heap >> child node < parent node   >>  root node greatest element

# time complexity  O(1) = constant best case complexity

# insertion of minheap into array :
# 1. create a empty heap with size n/2
# 2. start from last non leaf node and insert all the elements in heap ...
# 3. once all are inserted , swap the root element with last element of heap .....
# 4. reduce the size of heap by  1 ......
# 5. heapify the root element.................


# delete operation is not allowed in Heap data structure


# Heap Sort Algorithm:   complete binary tree  

# n = 2^k -1
# n+1 = 2^k
# log_2(n+1) = log_2 2^k
# log_2(n+1) = k
# k = log_2(n+1)    comparison =log_2(n+1) , swap = log_2(n+1)
# no of element = n
# insertion  time complexity = O(log_2(n)) worst case

# if the no of elements = n*2^n
# then the time complecxity=log(n*2^n)
# = log n + log*2^n

# in the case of deletion , deletionn happens from the root node and last element of the heap is taken to the root node . 
# so condtion for min heap violated and to validate the heap root element is compare to the both child element 
# so comparison happen 2*logn (for both left and right child  ) from root node and continue to the leaf node
 
# number of swap log_2(n)


# heap sort is comparison based sorting alagorithm : 
# when ever we delete an element the smallest elemet is deleted if we append this deleted element in a array
# we get sorted element in ascending order from min heap 

# for max heap we get descending order of elements . as greatest element was deleted
    
# overall time complecxity depends on the of comparison and no of swaps
# for each deletion time complexity is O(log_2(n))
# and for deletion of  n number of eliments  n*logn
# so for sorting the overall timecomplexity is O(nlog_2(n))


# time complexity to build a heap is O(n) >> heapfy method
# space complexity is O(1)

# derivation:

# # https://www.youtube.com/watch?v=AxALCZMo01Y&list=PLZoTAELRMXVPLDezwZ74wFhXvV5PaA2G2&index=7

# hapsort alagorithm:
# 1. build a min heap or max heap from the array (increasing or decreasing sorted function) >>O(n)
# 2. delete all the elements step by step  (and share those deleted element in any data structure) >>O(nlog_2(n))

# time complecxity = O(nlog_2(n)) +O(n) >> O(nlog_2(n))

# implementation : using heapq package:

# k frequent points

from collections import Counter
import heapq
def topKfrequentElement(arr, k):
    if k == len(arr):
        return set(arr)
    
    count = Counter(arr)
    # count is dictionary whiich contains unique values as the key and the frequency of those unique wlments as the value                           
    print(count)
    return heapq.nlargest(k, count.keys(), key=count.get)

    


## driver code
arr = [1,1,1,1,2,2,2,3]
# k = 2
# result = topKfrequentElement(arr,k)
# print("The top k frequent elements are: ",result)

# k closet points of k number
#eucladian distance

from heapq import heappush, heappop, heapify
import math

def get_dist(x, y):
    return math.sqrt(x**2 + y**2) # calculate eucladian distance
def kClosets(points,k):
    min_heap = []
    n = len(points)
    for i in range(n):
        x=points[i][0]
        y=points[i][1]
        #to insert the  point inside the minheap
        heappush(min_heap,(get_dist(x,y),points[i])) ## min heap store as dict key,value pair

    result = []
    for i in range(k):
        result.append(heappop(min_heap)[1]) #pop or delete min key  from the heap and append to the list retun value ie points cordinate

    return result

#dirver code
points = [[3,3],[5,-1],[-2,4]] 
k = 2
result = kClosets(points, k)
print("k closet points to the origin are :", result)

#rigt time to buy and sell stock

def findmaxProfit(prices):
    min_price = float('inf')
    max_profit =0

    for i in range(len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        elif prices[i] -min_price > max_profit:
            max_profit = prices[i] - min_price
    
    return max_profit



#driver code
prices = [7,1,5,3,6,4]
## function calling
maxProfit = findmaxProfit(prices)
print("max profit is :", maxProfit)

#time complexity: O(n)
#space complexity: O(1)

#finding of maxima and minima in an array in Brute force method

arr = [70,50,45,10,12,15,75,29,37,57]

