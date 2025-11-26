# An array of boolean values is divided into two sections: 
# The left section consists of all false, and the right section consists of all true.
#  Find the First True in a Sorted Boolean Array of the right section, i.e., the index 
# of the first true element. If there is no true element, return -1.

def find_boundary(arr):
    n = len(arr)

    l = 0
    r = n-1

    first_possible_true = -1

    while l <= r:
        m = l + ((r-l)//2)

        if arr[m] is True:
            first_possible_true = m
            r = m-1
        else:
            l = m+1
    return first_possible_true

arr = [False, False, False, True, True]
print(find_boundary(arr))