"""
 Merge two linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def CompareLists(headA, headB):
    tempA = headA
    tempB = headB
    while(True):
        if tempA.data != tempB.data :
            return 0 
        elif tempA.next is None and tempB.next is None:
            return 1
        elif tempA.next is None or tempB.next is None:
            return 0
        else:
            tempA = tempA.next
            tempB = tempB.next
    
  
  
  
  
  
  
  
  
  
  
  
  
  
