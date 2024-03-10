from src.models.explorator import Explorator

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

class Weapon(Item):
    """
    Classe de armas que podem ser usadas pelo explorador.
    """

    def __init__(self, name: str, description: str, usability: int, damage: int):
        super().__init__(name, description, usability)
        self.__damage = damage

    def getDamage(self) -> int:
        """
        Retorna o valor de dano da arma.\n
        Leva em consideração a usabilidade.
        """
        if self.getUsability() <= 0:
            return 0
        return self.__damage
    
    def tostring(self) -> str:
        return f'Weapon: [Damage: {self.getDamage()}, Usability: {self.getUsability()}]'

class Cure(Item):
    """
    Classe de itens de cura que podem ser usados pelo explorador.
    """

    def __init__(self, name: str, description: str, usability: int, heal: int) -> None:
        super().__init__(name, description, usability)
        self.__heal = heal
    
    def getHeal(self) -> int:
        """
        Retorna o potencial de cura do item.\n
        Leva em consideração a usabilidade.
        """
        if self.getUsability() > 0:
            return self.__heal
        return 0
        
    def use(self, explorator: Explorator) -> None:
        if super().use():
            explorator.setHeal(self.getHeal())
            
    def tostring(self) -> str:
        return f'Cure: [Heal: {self.getHeal()}, Usability: {self.getUsability()}]'
