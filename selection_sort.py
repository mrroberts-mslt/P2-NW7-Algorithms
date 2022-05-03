import random

def selection_sort(L):

    swaps = 0
    comparisons = 0
    #print("Before: ", L)
    
    # Traverse over all list elements
    for i in range(len(L)):
        
        # Find the minimum to the right of i
        min_idx = i
        for j in range(i+1, len(L)):
            comparisons = comparisons + 1
            if L[j] < L[min_idx]:
                min_idx = j
        
        # Swap minimum element with the current element
        L[i], L[min_idx] = L[min_idx], L[i]
        swaps = swaps + 1

    #print("After: ", aList)
    print("Summary: N (%d), #Comparisons (%d), #Swaps (%d)" %(len(L), comparisons, swaps))

# Driver code ...
# ... run this code for a list sizes 5, 10, 100 and 1000
# ... run for already sorted, reversed and randomised lists
# ... record the #comparisons and #swaps in the manual
aList = list(range(5)) # generate the ordered list
#aList.reverse() # reverse the list
#random.shuffle(aList) # randomise the list
selection_sort(aList)

# Tasks
# 1. Verify that #comparisons is approx (N^2)/2
# 2. Verify that #swaps is always N. Is this really necessary?

# Possible modifications/extensions:
# 1. Prompt the user to enter the size of the list, N
# 2. Prompt the user to enter whether the list should be already sorted, reversed or random
# 3. Display the number of comparisons and swaps for each pass
# 4. Display the actual values involved


'''
print("%s \t %s" %("Size", "Time(ms)"))
for list_size in [10, 1000, 2000, 4000, 8000]:
    L = list(range(list_size))
    L.reverse()
    t1 = time.time()
    selection_sort(L)
    t2 = time.time()
    print("%d \t %.1f" %(len(L), ((t2-t1) * 1000))) 
'''
