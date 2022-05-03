import random

def bubble_sort(L):

    swaps = 0
    comparisons = 0
    N = len(L)
    print("Before: ", L)

    # Traverse over all list elements
    for i in range(N):
        # Last i elements are already in place

        for j in range(N-1):

            comparisons = comparisons + 1
            # if the element is greater than the next element swap
            if aList[j] > aList[j+1]:
                # Swap L[j] with its next element
                L[j], L[j+1] = L[j+1], L[j]
                swaps = swaps + 1

    print("After: ", L)
    print("Summary: N (%d), #Comparisons (%d), #Swaps (%d)" %(N, comparisons, swaps))

# Driver code ...
# ... run this code for a list sizes 5, 10, 100 and 1000
# ... run for already sorted, reversed and randomised lists
# ... record the #comparisons and #swaps in the manual
aList = list(range(10)) # generate the ordered list
#aList.reverse() # reverse the list
#random.shuffle(aList) # randomise the list
bubble_sort(aList)

# Extension Tasks ....
# 1. Explain why for j in range(0, N-i-1): would be more efficient inner loop
# 2. Modify code so that it sorts list in descending order
# 3. Implement using while loops instead of for loops
# 4. Use a (boolean) flag to detect early completion
#(Hint: No swaps means list is already sorted)