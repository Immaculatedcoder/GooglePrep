# Write a function, get_node_value, that takes in the head of a linked list and an index. 
# The function should return the value of the linked list at the specified index.

# If there is no node at the given index, then return None.

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def get_node_value(head, index):
    current_node = head

    if index == 0:
        return current_node.val
    

    for _ in range(index):
        if current_node is None:
            break
        current_node = current_node.next

    if current_node is None:
        return None
    return current_node.val

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

print(get_node_value(a, 7))