from src.models.graph import Graph, Vertex
from enum import Enum
from random import choice

class Mark(Enum):
    WHITE = 0
    GRAY = 1
    BLACK = 2

def deepSearch(graph: Graph, startVertex: Vertex) -> list[int]:
    """
    Retorna uma lista de vértices a partir de uma busca em profundidade no grafo.
    """
    def visita(graph: Graph, vertex: Vertex, searchStack: list[Vertex]) -> list[Vertex]:
        searchStack.append(vertex)
        for u in graph.getAdjacentList(vertex):
            if u.getMark() == Mark.WHITE:
                path.append(u.getValue())
                u.setMark(Mark.GRAY)
                visita(graph, u, searchStack)
                path.append(vertex.getValue())
        vertex.setMark(Mark.BLACK)
        searchStack.pop()

    searchStack = []
    path: list[int] = []

    if graph.hasVertex(startVertex):
        for vertex in graph.getVertexs():
            vertex.setMark(Mark.WHITE)
        graph.get(startVertex.getValue()).setMark(Mark.GRAY)
        path.append(startVertex.getValue())
        visita(graph, startVertex, searchStack)
    return path

def  breadthFirstSearch(graph: Graph, startVertex: Vertex) -> list[int]:
    """
    Retorna uma lista de vértices a partir de uma busca em largura no grafo.
    """
    path: list[int] = []
    father: dict[int, int] = {}

    for vertex in graph.getVertexs():
        vertex.setMark(Mark.WHITE)
        father[vertex.getValue()] = startVertex.getValue()

    searchQueue: list[Vertex] = []
    searchQueue.insert(0, startVertex)

    startVertex.setMark(Mark.GRAY)

    while len(searchQueue) > 0:
        u = searchQueue.pop()
        path.append(u.getValue())
        for neighborn in graph.getAdjacentList(u):
            if neighborn.getMark() == Mark.WHITE:
                father[neighborn.getValue()] = u.getValue()
                neighborn.setMark(Mark.GRAY)
                searchQueue.insert(0, neighborn)
        u.setMark(Mark.BLACK)
        
        if len(searchQueue) > 0:
            lastValue = path[-1]
            while lastValue != startVertex.getValue():
                lastValue = father[lastValue]
                path.append(lastValue)
            nextValueFather = father[searchQueue[-1].getValue()]
            if nextValueFather != path[-1]:
                nextValuePath = [nextValueFather]
                while nextValuePath[-1] != startVertex.getValue():
                    nextValuePath.append(father[nextValuePath[-1]])
                nextValuePath.pop()
                path.extend(nextValuePath[::-1])
            
    return path

def randomSearch(graph: Graph, vertex: Vertex):
    return choice(graph.getAdjacentList(vertex))

def createWeights(graph: Graph) -> list[list]:
    weights: dict[dict] = {}
    for v in graph.getVertexs():
        weights[v.getValue()] = {}
        for w in graph.getVertexs():
            if v == w:
                weights[v.getValue()][w.getValue()] = 0
            elif graph.isConnected(v, w):
                weights[v.getValue()][w.getValue()] = 1
            else:
                weights[v.getValue()][w.getValue()] = 1_000_000_000
    return weights
