'''
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
'''

def subsets(nums):
    n = len(nums)
    res = []
    sol = []

    def backtrack(i):
        # Base case:
        if i == n:
            res.append(sol[:])
            return
        
        # Choice 1: If we decide to append the current nums[index]
        sol.append(nums[i]) 
        # We backtrack on this next index
        backtrack(i+1)
        # Undo or action
        sol.pop()


        #Choice 2: If we decide not to append
        backtrack(i+1)


    backtrack(0)
    return res   

nums = [1,2]
print(subsets(nums))