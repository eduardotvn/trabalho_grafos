from .item import Item

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
    