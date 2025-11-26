# Given an array (list) nums consisted of only non-negative integrers, find the largest sum among all subarray of length k in nums

# E.g nums = [1, 2, 3, 7, 4, 1] K = 3


def subarray_sum_fixed(nums, k):
    
    cur_sum = sum(nums[0:k])
    max_sum = cur_sum
    for r in range(k, len(nums)):
        l = r - k
        cur_sum = cur_sum + nums[r] - nums[l]
        max_sum = max(cur_sum, max_sum)
    return max_sum


nums = [1,2,3,7,4,1] 

k = 3

print(subarray_sum_fixed(nums,k))



