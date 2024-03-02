from src.models.item import Item

class Vertex():
    """
    Representação dos vértices do grafo
    """

    def __init__(self, value) -> None:
        self.__value = value
        self.__itens = []

    def getValue(self) -> int:
        """
        Retorna o valor único de um Vertex.
        Esse valor é usado para indexar o Vertex no grafo.
        """
        return self.__value
    
    def getVertexItens(self) -> list[Item]:
        """
        Retorna a lista de itens do Vertex.
        """
        return self.__itens
    
    def addItem(self, item: Item) -> None:
        """
        Adiciona um item ao Vertex.
        """
        self.__itens.append(item)

    def removeItem(self, item: Item) -> Item:
        """
        Remove o item passado da lista de itens do vértice.\n
        Retorna o item caso sucesso e None caso o item não exista.
        """
        if item in self.__itens:
            self.__itens.remove(item)
            return item
        return None 

class Graph():
    """
    Representação de um grafo por listas de adjacências.
    """

    def __init__(self, directional) -> None:
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
    
    def getAdjacentList(self, v:Vertex) -> list[Vertex]:
        """
        Retorna a lista de adjacência do vértice passado.
        """
        return self.__adjacentList[v.getValue()]

    def getVertexs(self) -> set[Vertex]:
        """
        Retorns um set contendo os vértices do grafo.
        """
        return self.__vertexs.values()

    def getVertexsValues(self) -> set[int]:
        """
        Retorna um set contendo os valores de cada vértice do grafo.
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
        v: Vertex
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
        if (self.hasNotVertex(v)): 
            self.addVertex(v)
        if (self.hasNotVertex(w)):
            self.addVertex(w)
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
    
    def tostring(self) -> str:
        graph = ''
        for vertex in self.getVertexs():
            graph += f'{vertex.getValue()}:'
            for edge in self.getAdjacentList(vertex):
                graph += f' {edge.getValue()} '
            graph += '\n'
        return graph

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