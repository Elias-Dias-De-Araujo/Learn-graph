class Graph:
    def __init__(self):
        self.graph = {}

    def addEdge(self, u, v, weight):
        self.graph[u, v] = weight

    def showMatrixGraph(self):
        print('Arestas e pesos: ')
        keys = self.graph.keys()
        for i in keys:
            print(str(i) + " : " + str(self.graph.get(i)))


gp = Graph()
gp.addEdge("A", "B", 1)
gp.addEdge("C", "A", 5)
gp.addEdge("D", "E", 7)
gp.addEdge("E", "A", 5)
gp.addEdge("D", "B", 7)
gp.addEdge("D", "L", 7)
gp.addEdge("W", "L", 7)
gp.showMatrixGraph()
