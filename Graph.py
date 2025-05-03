class Graph():
    def __init__(self,nv):
        self.nv = nv
        self.list = [[] for i in range(self.nv)]
    def createdges(self,v1,v2):
        self.list[v1].append(v2)
        self.list[v2].append(v1)


object = Graph(4)
object.createdges(0,1)
object.createdges(1,2)
object.createdges(2,3)
object.createdges(0,2)
object.createdges(1,3)
print(object.list)

