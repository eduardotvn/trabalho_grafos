from src.models.item import Item

class Vertex():
    """
    Representação dos vértices do grafo
    """

    def __init__(self, value) -> None:
        self.__value = value
        self.__mark = None
        self.__minCost = None
        self.__minCostFather = None
        self.__itens = []
        self.__checkpoint = False
        self.__treasure = 0

    def getValue(self) -> int:
        """
        Retorna o valor único do Vértice.
        Esse valor é usado para indexar o Vértice no grafo.
        """
        return self.__value
    
    def getMark(self):
        """
        Retorna o valor da marcação do vértice.
        """
        return self.__mark
    
    def setMark(self, mark) -> None:
        """
        Altera o valor da marca do vértice.
        """
        self.__mark = mark
    
    def getVertexItens(self) -> list[Item]:
        """
        Retorna a lista de itens do Vértice.
        """
        return self.__itens
    
    def getIsCheckPoint(self) -> bool:
        """
        Retorna se o vértice é um CheckPoint
        """
        return self.__checkpoint
    
    def setCheckPoint(self):
        """
        Transforma o vértice num CheckPoint
        """
        self.__checkpoint = True
        
    def getHasTreasure(self):
        """
        Verifica se é o vértice do tesouro
        """
        return self.__treasure > 0 
    
    def setTreasure(self):
        self.__treasure = 100

    def getMinCost(self) -> int:
        return self.__minCost
    
    def setMinCost(self, cost: int) -> None:
        self.__minCost = cost

    def getMinCostFather(self) -> int:
        return self.__minCostFather
    
    def setMinCostFather(self, value: int) -> None:
        self.__minCostFather = value

    def addItem(self, item: Item) -> None:
        """
        Adiciona um item ao Vértice.
        """
        self.__itens.append(item)

    def removeItem(self, item: Item) -> Item | None:
        """
        Remove o item passado da lista de itens do vértice.\n
        Retorna o item caso sucesso e None caso o item não exista.
        """
        if item in self.__itens:
            self.__itens.remove(item)
            return item
        return None 
    
    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Vertex):
            return self.getValue() == __value.getValue()
        return False
    
    def __str__(self) -> str:
        return f'Vertex: {self.getValue()}'

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
        if not self.isDirectional():
            self.getAdjacentList(w).append(v)
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