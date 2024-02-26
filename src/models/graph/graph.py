from models.itens.item import Item

class Vertex():
    __value = 0

    def __init__(self) -> None:
        self.__value = Vertex.__value
        Vertex.__value += 1
        self.__itens = []

    def getValue(self) -> int:
        return self.__value
    
    def getVertexItens(self) -> list[Item]:
        return self.__itens
    
    def addItem(self, item: Item) -> None:
        self.__itens.append(item)

class Graph():
    """
    Representação de um grafo por listas de adjacências.
    """
    def __init__(self) -> None:
        self.__vertexs: dict[list] = {}

    def addVertex(self, v:Vertex) -> None:
        """
        Adiciona um novo vértice no grafo.
        v: Vertex
        """
        self.__vertexs[v.getValue()] = []

    def addEdge(self, v:Vertex, w:Vertex, directional=False) -> None:
        """
        Adicona uma nova aresta segundo a representação de listas de adjacências.\n
        Se directional for False a adição considera o grafo não direcionado, caso True direcionado. 
        """
        self.__vertexs[v.getValue()].append(w)
        if not directional:
            self.__vertexs[w.getValue()].append(v)

v1 = Vertex()
v2 = Vertex()
print(v1.getValue())
print(v2.getValue())