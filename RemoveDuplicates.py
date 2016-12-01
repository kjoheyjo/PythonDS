"""
 Delete duplicate nodes
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def RemoveDuplicates(head):
    current = head
    while(current.next is not None):
        if(current.data == current.next.data):
            temp = current.next
            current.next = temp.next
            temp.next = None
        else:
            current = current.next
  
    return head
  
  
  
  
  
  
  
