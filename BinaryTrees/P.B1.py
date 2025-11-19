# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def max_path_sum(root):
  if root is None:
    return float('-inf')
  if root.left is None and root.right is None:
    return root.val

  left_path = max_path_sum(root.left)
  right_path = max_path_sum(root.right)
  return root.val + max(left_path, right_path)