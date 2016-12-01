"""
 Delete Node at a given position in a linked list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method. 
"""

def Delete(head, position):
    pos = 0
    temp = head
    while(True):
        if position==0:
            head = temp.next
            return head
        else:
            pos = pos + 1
            if pos == position:
                p = temp.next
                temp.next = p.next
                return head
            else:
                temp = temp.next
       
        
  
  
  
  
  
