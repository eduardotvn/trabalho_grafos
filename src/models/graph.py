from item import Item

class Vertex():
    """
    Representação dos vértices do grafo
    """
    # Cada instância de Vertex recebe um valor único crescente a parir de 0
    __value = 0

    def __init__(self) -> None:
        self.__value = Vertex.__value
        Vertex.__value += 1
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
    def __init__(self) -> None:
        self.__vertexs: dict[list[Vertex]] = {}
        self.__m = 0
        self.__n = 0

    def addVertex(self, v:Vertex) -> None:
        """
        Adiciona um novo vértice no grafo.
        v: Vertex
        """
        self.__vertexs[v.getValue()] = []
        self.__n += 1

    def addEdge(self, v:Vertex, w:Vertex, directional=False) -> None:
        """
        Adicona uma nova aresta segundo a representação de listas de adjacências.\n
        Se directional for False a adição considera o grafo não direcionado, caso True direcionado. 
        """
        if (v.getValue() not in self.__vertexs.keys()): 
            self.addVertex(v)
        if (w.getValue() in self.__vertexs.keys()):
            self.addVertex(w)

        self.__vertexs[v.getValue()].append(w)
        if not directional:
            self.__vertexs[w.getValue()].append(v)
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
        return self.__m

    def getNeighbors(self, v:Vertex) -> list[Vertex]:
        """
        Se existir, retorna a lista de adjacência do vértice.\n
        Caso contrario retorna None.
        """
        if v in self.__vertexs.keys():
            return self.__vertexs[v.getValue()]
        return None
    
    def getVertexs(self) -> set:
        """
        Retorna um set contendo os valores de cada vértice do grafo.
        """
        return self.__vertexs.keys()
    