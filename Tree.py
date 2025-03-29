class Tree():
    def __init__(self,data):
        self.data = data 
        self.left_node = None
        self.right_node = None
def inordertraversel(root):
    #L Ro R
    if root.left_node != None:
        inordertraversel(root.left_node)
    print(root.data)
    if root.right_node != None:
        inordertraversel(root.right_node)

def preordertravresel(root):
    print(root.data)
    if root.left_node != None:
        preordertravresel(root.left_node)
    if root.right_node != None: 
        preordertravresel(root.right_node)

def postordertraveresel(root):
    if root.left_node != None:
        postordertraveresel(root.left_node)
    if root.right_node != None:
        postordertraveresel(root.right_node) 
    print(root.data)

#MAKING THE TREE
root = Tree(10)
root.left_node = Tree(5)
root.left_node.left_node = Tree(5)
root.left_node.right_node = Tree(4)
root.right_node = Tree(2)
#inordertraversel(root)
#preordertravresel(root)
postordertraveresel(root)
