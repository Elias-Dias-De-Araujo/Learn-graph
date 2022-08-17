class Graph:
    def __init__(self, vertex):
        self.vertex = vertex
        self.graph = [[0]*self.vertex for i in range(self.vertex)]

    def addEdge(self, u, v):
        self.graph[u-1][v-1] = 1

    def showMatrixGraph(self):
        print('Matriz de adjacência: ')
        for i in range(self.vertex):
            print(self.graph[i])


gp = Graph(6)
gp.addEdge(1, 5)
gp.showMatrixGraph()
