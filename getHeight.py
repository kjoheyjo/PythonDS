def getHeight(self,root):
        if  root is None:
            return 0
        elif root.right is None and root.left is None: 
            return 0
        else:
            height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        
        return height