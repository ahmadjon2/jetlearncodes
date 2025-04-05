class Tree():
    def __init__(self,data):
        self.data = data 
        self.rightnode = None
        self.leftnode = None
def inorderstaversal(root):
    if root.leftnode != None:
        inorderstaversal(root.leftnode)
    print(root.data)
    if root.rightnode != None:
        inorderstaversal(root.rightnode)
def insertdata(root,data):
    if root == None:
        return Tree(data)
    if data > root.data:
        root.rightnode = insertdata(root.rightnode,data) 
    if data < root.data:
        root.leftnode = insertdata(root.leftnode,data)       
    return root
root = None
root = insertdata(root,7)
root = insertdata(root,5)
root = insertdata(root,6)
root = insertdata(root,85)

inorderstaversal(root)
