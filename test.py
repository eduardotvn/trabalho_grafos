from src.models.search import Graph, createWeights, Vertex

g = Graph()
g.addEdge(Vertex(1), Vertex(2))
g.addEdge(Vertex(1), Vertex(3))
g.addEdge(Vertex(1), Vertex(4))
g.addEdge(Vertex(2), Vertex(4))
g.addEdge(Vertex(4), Vertex(3))

print(createWeights(g))
print()
print(g.tostring())