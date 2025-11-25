# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_to_index = defaultdict(int)

        for i in range(len(nums)):
            remaining = target - nums[i]

            if remaining in value_to_index:
                return [i, value_to_index[remaining]]
            else: 
                value_to_index[nums[i]] = i