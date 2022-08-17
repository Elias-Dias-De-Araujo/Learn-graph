class Graph:
    def __init__(self, vertex):
        self.vertex = vertex
        self.graph = [[0]*self.vertex for i in range(self.vertex)]

    def addEdge(self, u, v, weight):
        self.graph[u-1][v-1] = weight

    def showMatrixGraph(self):
        print('Matriz de adjacência ( pesos ): ')
        for i in range(self.vertex):
            print(self.graph[i])


gp = Graph(6)
gp.addEdge(1, 5, 4)
gp.addEdge(2, 4, 2)
gp.addEdge(3, 2, 6)
gp.addEdge(4, 5, 1)
gp.showMatrixGraph()
