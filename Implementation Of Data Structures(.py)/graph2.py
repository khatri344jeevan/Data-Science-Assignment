class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []
            
    def add_edge(self, u, v):
        self.add_node(u)
        self.add_node(v)
        self.graph[u].append(v)
        self.graph[v].append(u)
    def display(self):
        print(self.graph)

g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.display()