"""
 Insert Node at the end of a linked list 
 head pointer input could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node
 
 return back the head of the linked list in the below method
"""

def Insert(head, data):
    temp =  head
    while(True):
        if  temp is None:
            f = Node()
            f.data = data
            f.next = None
            head = f
            return head
        elif temp.next is None:
            f = Node()
            f.data = data
            f.next = None
            temp.next = f
            return head
        else:
            temp = temp.next
         


  
  
  
  
  
  
