"""
 Insert Node at a specific position in a linked list
 head input could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method. 
"""
#This is a "method-only" submission.
#You only need to complete this method.
def InsertNth(head, data, position):
    pos = 0
    f = Node()
    f.data = data
    temp = head
    while(True):
        if position==0:
            f.next = head
            head = f
            return head
        else:
            pos = pos + 1
            if pos==position:
                f.next = temp.next
                temp.next = f
                return head
            else:
                temp = temp.next
                
                
            
            
        
    
  
  
  
  
  
  
  
  
  
  
