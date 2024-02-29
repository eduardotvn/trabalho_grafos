
class Item():
    pass

class Weapon(Item):

    def __init__(self, usability, damage):
        self.__usability = usability
        self.__damage = damage

    def getDamage(self) -> int:
        """
        Retorna o valor de dano da arma.\n
        Leva em consideração a usabilidade.
        """
        if self.__usability <= 0:
            return 0
        return self.__damage
    
    def getUsability(self) -> int:
        """
        Reorna a quantidade de usos restantes da arma.
        """
        return self.__usability
    
    def use(self) -> None:
        """
        Diminue em um a usabilidade da arma.
        """
        if self.__usability > 0:
            self.__usability -= 1
    
    def tostring(self) -> str:
        return f'Weapon: [Damage: {self.getDamage()}, Usability: {self.getUsability()}]'

