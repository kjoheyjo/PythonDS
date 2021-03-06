"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    current = head
    while(current.next is not None):
        if(current.data is None):
            return True
        else:
            temp = current
            current = current.next
            temp.data = None
        
    
    
    
    
