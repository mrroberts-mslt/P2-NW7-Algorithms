import random

def binary_search(v, L):
    global comparisons
    
    low = 0
    high = len(L)-1

    while (low <= high):
        comparisons = comparisons + 1
        
        mid = (low+high)//2
        
        if L[mid] == v:
            return mid
        elif L[mid] < v:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1


# Driver code ...
print("%s\t\t %s\t\t %s" %("List Size", "Found Index", "#Comparisons"))
for list_size in [1, 10, 100, 1000, 10000, 100000, 1000000]:
    some_list = list(range(list_size))
    comparisons = 0
    target = -1 # worst case because -1 never exists
    pos = binary_search(target, some_list)
    print("%d\t\t %d\t\t %d" %(len(some_list), pos, comparisons))
