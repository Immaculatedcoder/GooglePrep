# Classical Level Order Traversal
import collections
class Node:
    def __init__(self, val = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


a = Node(1)
b = Node(2)
c = Node(3)

a.left = b
a.right = c

def level_order_traversal(root):
    q = collections.deque()
    q.append(root)
    result = []
    while q:
        current_node = q.popleft()
        result.append(current_node.val)

        if current_node.left:
            q.append(current_node.left)
        if current_node.right:
            q.append(current_node.right)

    return result

print(level_order_traversal(a))





