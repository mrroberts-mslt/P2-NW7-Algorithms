import random
import time

def linear_search(v, L):
    
    for index in range(len(L)):
        if L[index] == v:
            return index
            
    return -1


def binary_search(v, L):
    
    low = 0
    high = len(L)-1

    while (low <= high):
        
        mid = (low+high)//2
        
        if L[mid] == v:
            return mid
        elif L[mid] < v:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1


# Driver code ...
some_list = list(range(1000000))
target = -1 # worst case because -1 never exists

start_time = time.perf_counter()
pos = linear_search(target, some_list)
#pos = binary_search(target, some_list)
end_time = time.perf_counter()

# difference of start and end times gives the execution time
print("List Length (%d) \t Execution Time (%f)" %(len(some_list), (end_time-start_time) ))

# Conclusion:
# Time is not a good measure of performance (because it is machine dependent)
