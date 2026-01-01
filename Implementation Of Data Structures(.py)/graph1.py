import networkx as nx

G = nx.Graph()
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(2, 4)

print("Edges:", G.edges())
print("Nodes:", G.nodes())