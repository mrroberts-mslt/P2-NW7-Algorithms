import random

def insertion_sort(L):

    swaps = 0
    comparisons = 0
    #print("Before: ", L)

    # Traverse over all list elements
    for i in range(1, len(L)):
        
        # Uncomment next line to the state of the list on each pass
        # print("Pass: ", i, L)
        
        # Bubble L[i] into its correct sorted position
        j = i
        comparisons = comparisons + 1
        while j>0 and L[j] < L[j-1]:
            # Swap L[j] with its previous element
            L[j], L[j-1] = L[j-1], L[j]
            j = j-1
            swaps = swaps + 1
            comparisons = comparisons + 1

    #print("After: ", L)
    print("N(%d), #Comparisons(%d),#Swaps(%d)"%(len(L),comparisons, swaps))

# Driver code ...
# ... run this code for a list sizes 5, 10, 100 and 1000
# ... run for already sorted, reversed and randomised lists
# ... record the #comparisons and #swaps in the manual
aList = list(range(10000)) # generate the ordered list
#aList.reverse() # reverse the list
random.shuffle(aList) # randomise the list

insertion_sort(aList)

# Task. Investigate the proposition ...
# Proposition. For randomly ordered arrays of length N with with distinct values,
# insertion sort uses ~(N^2)/4 compares and ~(N^2)/4 swaps on the average.
# The worst case is ~ (N^2)/2 compares and ~ (N^2)/2 swaps and
# the best case is N-1 compares and 0 swaps.


'''
# Extension Task ...
# insertion_sort_v2 defined below is an alternative to insertion_sort above
# Which algorithm is better (more efficient) in your opinion. Why?
def insert(value, A, pos):
    i = pos-1
    while i>=0 and A[i] > value:
        A[i+1] = A[i]
        i = i-1

    A[i+1] = value


def insertion_sort_v2(L):
    for i in range(1, len(L)):
        # insert L[i] into L before position i
        insert(L[i], L, i)

    return
    
# Driver code for V2 ...
the_list = [6, 1, 15, 12, 5, 6, 9]
print("Before:", the_list)
insertion_sort_v2(the_list)
print("After:", the_list)
'''
