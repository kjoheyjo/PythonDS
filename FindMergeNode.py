"""
 Find the node at which both lists merge and return the data of that node.
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 
"""

def FindMergeNode(headA, headB):
    A = headA
    B = headB
    
    while(A is not None):
        while(B is not None):
            if(A==B):
                return A.data
            else:
                B = B.next
        
        A = A.next
        B= headB
    
    
  
  
  
  
  
  
  
  
  
  
