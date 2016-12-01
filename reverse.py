"""
 Reverse a doubly linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None, prev_node = None):
       self.data = data
       self.next = next_node
       self.prev = prev_node

 return the head node of the updated list 
"""
def Reverse(head):
    if head is None:
            return
    else:
        current = head
        nextnode = head.next
        head.next = None
        while(nextnode is not None):
            if nextnode.next is None:
                nextnode.next = current
                current.prev = nextnode
                
                return nextnode
            else:
                temp = nextnode.next
            nextnode.next = current
            current.prev = nextnode

            current = nextnode
            nextnode = temp
                
        return head
                
        
        
        
  
  
  
  
  
  
  
  
