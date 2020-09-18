"""
Route Between Nodes: Given a directed graph, design an algorithm to find out whether there is a
route between two nodes.

Time Complexity O(E+V)
"""
from collections import defaultdict, deque

class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def routeFinder(self, src, des):
        visited = [0]*self.V
        queue = deque()
        queue.append(src)
        visited[src] = 1

        while queue:
            n = queue.pop()
            if n == d:
                return True
            for i in self.graph[n]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = 1
        return False

g = Graph(4) 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3)
            
        
        
        
