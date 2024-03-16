from .item import Item

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
        self.__treasure = False

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

    def unCheckPoint(self):
        """
        Remove o checkpoint do ponto
        """
        self.__checkpoint = False
        
    def getHasTreasure(self):
        """
        Verifica se é o vértice do tesouro
        """
        return self.__treasure  
    
    def setTreasure(self):
        self.__treasure = True

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
    