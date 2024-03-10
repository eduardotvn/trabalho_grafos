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
    def visit(graph: Graph, vertex: Vertex, searchStack: list[Vertex]) -> list[Vertex]:
        searchStack.append(vertex)
        for u in graph.getAdjacentList(vertex):
            if u.getMark() == Mark.WHITE:
                path.append(u.getValue())
                u.setMark(Mark.GRAY)
                visit(graph, u, searchStack)
                path.append(vertex.getValue())
        vertex.setMark(Mark.BLACK)
        searchStack.pop()

    searchStack = [] # pilha para armazenar o próximo vértice a ser explorado
    path: list[int] = [] # a ordem do percuso dos vértices em profundidade 

    if graph.hasVertex(startVertex):
        # todos os vértices devem começar como brancos
        for vertex in graph.getVertexs():
            vertex.setMark(Mark.WHITE)
        graph.get(startVertex.getValue()).setMark(Mark.GRAY) # o vértice inicial é marcado como cinza
        path.append(startVertex.getValue())
        visit(graph, startVertex, searchStack)
    return path

def  breadthFirstSearch(graph: Graph, startVertex: Vertex) -> list[int]:
    """
    Retorna uma lista de vértices a partir de uma busca em largura no grafo.
    """

    # a ordem do percuso dos vértices em profundidade
    path: list[int] = []
    # armazena, para cada vértice, o vértice pelo qual este (chave) foi acessado primeiramente.
    father: dict[int, int] = {}

    for vertex in graph.getVertexs():
        vertex.setMark(Mark.WHITE)
        father[vertex.getValue()] = startVertex.getValue()

    searchQueue: list[Vertex] = [] # fila para armazenar o próximo vértice a ser explorado
    searchQueue.insert(0, startVertex)

    startVertex.setMark(Mark.GRAY)

    # enquando a fila tiver elementos a busca continua
    while len(searchQueue) > 0:
        u = searchQueue.pop() # removendo o elemento mais antigo da fila
        path.append(u.getValue())
        for neighborn in graph.getAdjacentList(u):
            if neighborn.getMark() == Mark.WHITE:
                father[neighborn.getValue()] = u.getValue()
                neighborn.setMark(Mark.GRAY)
                searchQueue.insert(0, neighborn)
        u.setMark(Mark.BLACK)
        
        
        nextValuePath = []
        nextValueFather = startVertex.getValue()
        if len(searchQueue) > 0:
            '''
            Se a busca não chegou ao fim, então é gerado um caminho
            do vértice inicial até o pai do próximo vértice. 
            '''
            nextValueFather = father[searchQueue[-1].getValue()]
            if nextValueFather != path[-1]:
                nextValuePath.append(nextValueFather)
                while nextValuePath[-1] != startVertex.getValue():
                    nextValuePath.append(father[nextValuePath[-1]])
            nextValuePath = nextValuePath[::-1]

        lastValue = path[-1]
        while lastValue != nextValueFather:
            if lastValue in nextValuePath:
                '''
                Se o último vértice do percuso está contido no caminho do vértice
                inicial até o pai do próximo vértice da busca, então podemos usar
                esse caminho para chegar no próximo vértice.
                '''
                index = nextValuePath.index(lastValue)
                for i in range(index + 1, len(nextValuePath)):
                    path.append(nextValuePath[i])
                break
            '''
            Caso contrário adiciona-se o pai do último vértice ao percuso.
            Dessa forma ou chegaremos no pai do último vértice ou no vértice inicial,
            e assim usaremos o caminho já calculado.
            '''
            lastValue = father[lastValue]
            path.append(lastValue)
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
