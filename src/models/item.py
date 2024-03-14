
class Item():
    """
    Classe genérica de itens.
    """

    def __init__(self, name: str, description: str, usability: int) -> None:
        self.__name = name
        self.__usability = usability
        self.__description = description

    def getName(self) -> str:
        """
        Retorna o nome do item.
        """
        return self.__name
    
    def getUsability(self) -> int:
        """
        Reorna a quantidade de usos restantes do item.
        """
        return self.__usability
    
    def getDescription(self) -> str:
        """
        Retorna a descrição do item.
        """
        return self.__description
    
    def use(self) -> bool:
        """
        Se maior que zero, diminue em um a usabilidade do item e retorna Verdade.\n
        Rotorna False se o item não possui usabilidade.
        """
        if self.__usability > 0:
            self.__usability -= 1
            return True
        return False
