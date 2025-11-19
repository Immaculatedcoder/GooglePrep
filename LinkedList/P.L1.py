# Write a function, linked_list_values, that takes in the head of a linked list as an argument. 
# The function should return a list containing all values of the nodes in the linked list.

# Hey. This is our first linked list problem, so you should be liberal with watching the Approach and Walkthrough.
#  Be productive! -AZ

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def linked_list_values(head):
    if head is None:
        return []
    
    rest = linked_list_values(head.next)

    return [head, *rest]
