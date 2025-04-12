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
def search(root,data):
    if data == root.data:
        return root
    elif data < root.data and root.leftnode != None:
        return search(root.leftnode,data) 
    elif data > root.data and root.rightnode != None:
        return search(root.rightnode,data)
    else:
        return -1

root = None
root = insertdata(root,7)
root = insertdata(root,5)
root = insertdata(root,6)
root = insertdata(root,85)

inorderstaversal(root)
searching = search(root,99)
if searching == -1:
    print("the searched number is not there")
else:
    print("the searched number was found, ",root.data)


