"""
 Insert a node into a sorted doubly linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None, prev_node = None):
       self.data = data
       self.next = next_node
       self.prev = prev_node

 return the head node of the updated list 
"""
def SortedInsert(head, data):
    current = head
    f = Node()
    f.data = data
    if head is None:
        f.next = None
        f.prev = None
        return f
    elif  data<head.data:
        f.next = head
        head.prev = f
        f.prev = None
        return f
    else:
        rest = SortedInsert(head.next,data)
        head.next = rest
        rest.prev = None
        return head
            
            
            
            