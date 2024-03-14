from .vertex import Vertex

class Graph():
    """
    Representação de um grafo por listas de adjacências.
    """

    def __init__(self, directional=False) -> None:
        self.__directional: bool = directional
        self.__adjacentList: dict[int, list[Vertex]] = {}
        self.__vertexs: dict[int, Vertex] = {}
        self.__m: int = 0
        self.__n: int = 0

    def isDirectional(self) -> bool:
        """
        Retorna se o grafo é direcionado ou não.
        """
        return self.__directional
    
    def get(self, value: int) -> Vertex | None:
        """
        Retorna o vértice que possui o valor especificado, se existir.
        """
        if value in self.getVertexsValues():
            return self.__vertexs[value]
    
    def getAdjacentList(self, v:Vertex) -> list[Vertex]:
        """
        Retorna a lista de adjacência do vértice passado como argumento.
        """
        return self.__adjacentList[v.getValue()]

    def getVertexs(self) -> set[Vertex]:
        """
        Retorns um conjunto contendo os vértices do grafo.
        """
        return self.__vertexs.values()

    def getVertexsValues(self) -> set[int]:
        """
        Retorna um conjunto contendo os valores de cada vértice do grafo.
        """
        return self.__vertexs.keys()

    def hasVertex(self, v: Vertex) -> bool:
        """
        Retorna se um vértice pertence ou não pertence ao grafo. 
        """
        return v.getValue() in self.getVertexsValues()
    
    def hasNotVertex(self, v: Vertex) -> bool:
        """
        Retorna se um vértice não pertence ou pertence ao grafo. 
        """
        return not self.hasVertex(v)

    def addVertex(self, v:Vertex) -> None:
        """
        Adiciona um novo vértice no grafo.
        """
        if self.hasNotVertex(v):
            self.__vertexs[v.getValue()] = v
            self.__adjacentList[v.getValue()] = []
            self.__n += 1
    
    def addEdge(self, v:Vertex, w:Vertex) -> None:
        """
        Adicona uma nova aresta segundo a representação de listas de adjacências.\n
        Se os vértices não existirem no grafo eles serão adicionados.\n
        """
        if (self.hasNotVertex(v)): self.addVertex(v)
        if (self.hasNotVertex(w)): self.addVertex(w)
        self.getAdjacentList(v).append(w)
        self.__m += 1

    def getN(self) -> int:
        """
        Retorna a quantidade de vértices do grafo.
        """
        return self.__n
    
    def getM(self) -> int:
        """
        Retorna a quantidade de arestas do grafo.
        """
        if self.isDirectional():
            return self.__m
        return self.__m / 2
    
    def isConnected(self, v: Vertex, w: Vertex) -> bool:
        """
        Retorna se o vértice w está na vizinhança de v.
        """
        return w in self.getAdjacentList(v)
    
    def tostring(self) -> str:
        graph = ''
        for vertex in self.getVertexs():
            graph += f'{vertex.getValue()}:'
            for edge in self.getAdjacentList(vertex):
                graph += f' {edge.getValue()} '
            graph += '\n'
        return graph
    
    def __str__(self) -> str:
        return self.tostring()

def readGraph(filePath: str, directional=False) -> Graph:
    """
    Retorna um grafo a partir do arquivo lido.
    """
    graph = Graph(directional=directional)
    with open(filePath) as graphText:
        for line in graphText.readlines():
            line = line.strip().split(':')
            vertex = Vertex(int(line.pop(0)))
            graph.addVertex(vertex)
            
            vertexEdges = line.pop(0).strip().split(' ')
            for edge in vertexEdges:
                neighbor = Vertex(int(edge))
                graph.addEdge(vertex, neighbor)
    return graph