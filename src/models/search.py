from src.models.graph import Graph, Vertex
from enum import Enum
from random import choice
import heapq

class Mark(Enum):
    WHITE = 0
    GRAY = 1
    BLACK = 2

# Representação do infinito
INF = 2_000_000_000

def deepSearch(graph: Graph, startVertex: Vertex):
    searchStack = []
    for vertex in graph.getVertexs():
        vertex.setMark(Mark.WHITE)
    __visita(graph, startVertex, searchStack)

def __visita(graph: Graph, vertex: Vertex, searchStack: list[Vertex]):
    searchStack.append(vertex)
    for u in graph.getAdjacentList(vertex):
        if u.getMark() == Mark.WHITE:
            u.setMark(Mark.GRAY)
            __visita(graph, u, searchStack)
    vertex.setMark(Mark.BLACK)
    searchStack.pop()

def  breadthFirstSearch(graph: Graph, startVertex: Vertex):
    for vertex in graph.getVertexs():
        vertex.setMark(Mark.WHITE)
    searchQueue: list[Vertex] = []
    searchQueue.insert(0, startVertex)
    for u in searchQueue:
        for neighborn in graph.getAdjacentList(u):
            if neighborn.getMark() == Mark.WHITE:
                neighborn.setMark(Mark.GRAY)
                searchQueue.insert(0, neighborn)
        u.setMark(Mark.BLACK)

def randomSearch(graph: Graph, vertex: Vertex):
    return choice(graph.getAdjacentList(vertex))

def dijkstra(graph: Graph, startVertex: Vertex):
    weights = createWeights(graph)
    for vertex in graph.getVertexs():
        vertex.setMinCost(weights[startVertex.getValue()][vertex.getValue()])
        vertex.setMinCostFather(vertex.getValue())
    searchHeap = [(vertex.getMinCost(), vertex) for vertex in graph.getVertexs()]
    heapq.heapify(searchHeap)
    while len(searchHeap) != 0:
        _, u = heapq.heappop(searchHeap)

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
                weights[v.getValue()][w.getValue()] = INF
    return weights
