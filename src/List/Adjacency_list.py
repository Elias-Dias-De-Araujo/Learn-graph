class Graph:
    def __init__(self, vertex):
        self.vertex = vertex
        self.graph = [[]for i in range(self.vertex)]

    def addEdge(self, u, v):
        self.graph[u-1].append(v-1)

    def showListGraph(self):
        print('Lista de adjacência: ')
        for i in range(self.vertex):
            print(f'{i+1}:', end='  ')
            for j in self.graph[i]:
                print(f'{j+1}  ->', end='  ')
            print('')


gp = Graph(5)
gp.addEdge(1, 5)
gp.addEdge(2, 4)
gp.addEdge(3, 2)
gp.addEdge(4, 1)
gp.showListGraph()
