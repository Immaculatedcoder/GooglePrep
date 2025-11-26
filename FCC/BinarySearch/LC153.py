# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums of unique elements, return the minimum element of this array.

# You must write an algorithm that runs in O(log n) time

def find_min_rotated(arr):
    n = len(arr)
    l = 0
    r = n - 1

    first_min = -1
    while l <= r:
        m = l + ((r-l)//2)

        if arr[m] <= arr[-1]:
            first_min = m
            r = m - 1
        else:
            l = m + 1
    return arr[first_min]

arr = [0,1,2,3,4,5,6,7]
print(find_min_rotated(arr))


