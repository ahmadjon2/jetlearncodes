class Graph():
    def __init__(self,nv):
        self.nv = nv
        self.list = [[] for i in range(self.nv)]
    def createdges(self,v1,v2):
        self.list[v1].append(v2)
        self.list[v2].append(v1)
    def find_connected_components(self):                        
        visited = []
        cc = []
        for i in range(self.nv):
            visited.append(False)
        for i in range(self.nv):
            if visited[i] == False:
                temp = []
                cc.append(self.dfs_util(temp,i,visited))
        return cc
    def dfs_util(self,temp,i,visited):
        visited[i] = True
        temp.append(i)
        for j in self.list[i]:
            if visited[j] == False:
                temp = self.dfs_util(temp,j,visited)
        return temp
    

        
object = Graph(5)
object.createdges(0,1)
object.createdges(2,3)
object.createdges(3,4)
cc = object.find_connected_components()
print(cc)