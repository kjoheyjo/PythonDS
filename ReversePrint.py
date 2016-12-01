"""
 Print elements of a linked list in reverse order as standard output
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 
"""

def ReversePrint(head):
    temp = head
    if temp is None:
        return
    elif temp.next is None:
        print(temp.data)
        return
    else:
        ReversePrint(temp.next)
        print(temp.data)
        

  
  
  
  
    
