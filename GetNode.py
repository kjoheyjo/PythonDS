#Body
"""
 Get Node data of the Nth Node from the end.
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the node data of the linked list in the below method.
"""

def GetNode(head, position):
    current = head
    temp = head
    for i in range(0,position):
        current = current.next
     
    while(current.next is not None):
        temp = temp.next
        current = current.next
  
    return temp.data
  
  
  
  
  
  
