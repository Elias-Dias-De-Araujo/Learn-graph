class Graph:
    def __init__(self, vertex):
        self.vertex = vertex
        self.graph = {}

    def addEdge(self, u, v, weight):
        self.graph[u, v] = weight

    def showMatrixGraph(self):
        print('Matriz de adjacência: ')
        print(self.graph)


g = Graph(6)
g.addEdge("A", "B", 1)
g.addEdge("C", "A", 5)
g.addEdge("D", "E", 7)
g.addEdge("E", "A", 5)
g.addEdge("D", "B", 7)
g.addEdge("D", "L", 7)
g.addEdge("W", "L", 7)
g.showMatrixGraph()
