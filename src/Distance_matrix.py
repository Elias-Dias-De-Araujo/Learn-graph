class Graph:
    def __init__(self, vertex):
        self.vertex = vertex
        self.graph = [[0]*self.vertex for i in range(self.vertex)]

    def addEdge(self, u, v, weight):
        self.graph[u-1][v-1] = weight

    def showMatrixGraph(self):
        print('Matriz de adjacência: ')
        for i in range(self.vertex):
            print(self.graph[i])


test = Graph(6)
test.addEdge(1, 5, 4)
test.addEdge(2, 4, 2)
test.addEdge(3, 2, 6)
test.addEdge(4, 5, 1)
test.showMatrixGraph()
