'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
'''

def generateParenthesis(n):
    res = []
    sol = "("

    dict = {"(":1, ")":0}
    def backtrack():
        nonlocal sol
        if dict["("] == n and dict[")"] == n:
            res.append(sol[:])
            return
        
        if dict["("] > n:
            return
        
        if dict["("] < dict[")"]:
            return
        
        sol = sol + "("
        dict["("] += 1
        backtrack()
        sol = sol[:-1]
        dict["("] -= 1

        #Choice 2: Either we append )
        sol = sol + ")"
        dict[")"] += 1
        backtrack()
        sol = sol[:-1]
        dict[")"] -= 1

    backtrack()
    return res

n = 3
print(generateParenthesis(n))