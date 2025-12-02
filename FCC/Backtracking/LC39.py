'''
39. Combination Sum

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations
of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency
of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
'''

def combinationsum(candidates, target):
    n = len(candidates)
    res = []
    sol = []

    def backtrack(i):
        if sum(sol) == target:
            res.append(sol[:])
            return
        
        if sum(sol) > target:
            return
        
        if i == n:
            return
        
        # Choice 1: If we decide to pick i
        sol.append(candidates[i])
        backtrack(i)
        sol.pop()

        # Choice 2: If we decide not to pick i
        backtrack(i+1)

    
    backtrack(0)
    return res

candidates = [2,3,6,7]
target = 7
print(combinationsum(candidates,target))

    