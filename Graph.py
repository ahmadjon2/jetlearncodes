class Graph():
    def __init__(self,nv):
        self.nv = nv
        self.list = [[] for i in range(self.nv)]
    def createdges(self,v1,v2):
        self.list[v1].append(v2)
        self.list[v2].append(v1)
    def bfs(self,source):
        visited = [False]*self.nv
        res = []#the sequence
        queue = []
        queue.append(source)
        visited[source] = True
        while len(queue) > 0:
            s = queue.pop(0)
            res.append(s)
            for node in self.list[s]:# going through all the vertices connected with "s"
                if visited[node] == False:# To check if the node is already visited
                    visited[node] = True# marking it as visited
                    queue.append(node)
        return res  
    def dfs(self,source):   
        visited = [False]*self.nv
        res = []
        self.dfs_util(source, visited, res)
        return res
    
    def dfs_util(self, src, visited, res):
        res.append(src)
        visited[src] = True
        for node in self.list[src]:
            if visited[node] == False:
                self.dfs_util(node, visited, res)



object = Graph(4)
object.createdges(0,1)
object.createdges(0,2)
object.createdges(1,3)
object.createdges(2,3)

print(object.list)
store = object.bfs(0)
print(store)
store = object.dfs(0)
print(store)
