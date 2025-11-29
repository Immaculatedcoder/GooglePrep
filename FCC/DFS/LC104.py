'''
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)

a.left = b
a.right = c
b.left = d
b.right = e
d.left = f

# def dfs(root):
#   if root is None:
#     return

#   print(root.val)
#   dfs(root.left)
#   dfs(root.right)

# dfs(a)


def maxDepth(root):
    def dfs(root):
        if root is None:
            return

def maxDepth(root):
    def dfs(root):
        if root is None:
            return 0
        
        left = dfs(root.left)
        right = dfs(root.right)
        
        return 1 + max(right, left)
    return dfs(root) if root else 0

print(maxDepth(None))
