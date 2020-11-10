import math


root = [6,7,8,2,7,1,3,9,None,1,4,None,None,None,5]

print(int(math.sqrt(len(root)))+1)

class grandParentOfChild:
    def __init__(self,root,childIndex):
        self.childIndex = childIndex
        self.root = root

    def grandParentNode(self):
        if self.childIndex > 2:
            

#class nodeResultIfEvenGrandparent: