from .item import Item
from .trap import Trap

class Vertex():
    """
    Representação dos vértices do grafo
    """

    def __init__(self, value) -> None:
        self.__value = value
        self.__mark = None
        self.__itens = []
        self.__checkpoint = False
        self.__treasure = False
        self.__beginning = False
        self.__trap = None

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
    
    
    def getVertexItens(self) -> list[Item]:
        """
        Retorna a lista de itens do Vértice.
        """
        return self.__itens
    
    def isCheckPoint(self) -> bool:
        """
        Retorna se o vértice é um CheckPoint
        """
        return self.__checkpoint
    
    def isBeginning(self) -> bool:
        """
        Retorna se o vértice é um checkpoint.
        """
        return self.__beginning
    
    def hasTreasure(self) -> bool:
        """
        Verifica se é o vértice do tesouro
        """
        return self.__treasure  
    
    def hasTrap(self) -> bool:
        """
        Verifica se o vértice possui uma armadilha.
        """
        return self.__trap != None
    
    def setTrap(self, trap: Trap) -> None:
        """
        Atribui uma armadilha ao vértice.
        """
        self.__trap = trap

    def getTrap(self) -> Trap:
        """
        Retorna o objeto armadilha do vértice, se existir
        """
        if self.hasTrap():
            return self.__trap
    
    def setBeginning(self) -> None:
        """
        Altera o vértice para que ele seja o começo do grafo
        """
        self.__beginning = True
    
    def setMark(self, mark) -> None:
        """
        Altera o valor da marca do vértice.
        """
        self.__mark = mark
    
    def setCheckPoint(self) -> None:
        """
        Transforma o vértice num CheckPoint
        """
        self.__checkpoint = True

    def unSetCheckPoint(self) -> None:
        """
        Retira o CheckPoint do vértice.
        """
        self.__checkpoint = False

    def setTreasure(self):
        """
        Retorna True se o vértice contém o tesouro.
        """
        self.__treasure = True

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
    