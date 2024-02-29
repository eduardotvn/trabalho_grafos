from creature import Creature
from item import Weapon

class Explorator(Creature):

    def __init__(self, hp: int, attack: int) -> None:
        self.__weapon: Weapon = None
        self.__lastCheck = None
        super().__init__(hp, attack)

    def getWeapon(self) -> Weapon:
        """
        Retorna a arma segurada pelo explorador caso ela exista.
        """
        return self.__weapon

    def setWeapon(self, w: Weapon) -> None:
        """
        Altera a arma segurada pelo explorador para a arma passada.
        """
        self.__weapon = w

    def hasWeapon(self) -> bool:
        """
        Retorna se o explorador está ou não segurando uma arma.
        """
        return self.__weapon != None
    
    def setCheck(self, c: int) -> None:
        """
        Associa o explorador ao valor de um vértice do tipo Checkpoint.
        """
        self.__lastCheck = c

    def useCheck(self) -> int:
        """
        Se existir um valor de vértice Checkpoint a função o retorna.\n
        Caso contrário retorna None.
        Em seguida o atributo perde seu valor.\n
        """
        if self.__lastCheck:
            c = self.__lastCheck
            self.__lastCheck = None
            return c
        return None
    
    def getAttack(self) -> int:
        """
        Retorna o ataque do explorador considerando o dano adicional da arma.
        """
        attack = super().getAttack()
        if self.hasWeapon():
            attack += self.getWeapon().getDamage()
        return attack
    
    def attack(self) -> tuple[int, str]:
        if self.hasWeapon():
            self.getWeapon().use()
        return super().attack()
    