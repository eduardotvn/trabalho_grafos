from creature import Creature
from item import Weapon

class Explorator(Creature):

    def __init__(self, hp: int, attack: int) -> None:
        self.__weapon: Weapon = None
        self.__checks: list = []
        super().__init__(hp, attack)

    def getWeapon(self) -> Weapon:
        """
        Retorna a arma segurada pelo explorador caso ela exista.
        """
        return self.__weapon

    def setWeapon(self, weapon: Weapon) -> Weapon:
        """
        Altera a arma segurada pelo explorador para a arma passada. \n
        Retorna a arma segurada antes pelo explorador, caso exista.
        """
        oldWeapon = self.getWeapon()    
        self.__weapon = weapon
        if oldWeapon:
            return oldWeapon

    def hasWeapon(self) -> bool:
        """
        Retorna se o explorador está ou não segurando uma arma.
        """
        return self.__weapon != None
    
    def hasCheckpoint(self) -> bool:
        """
        Retorna se o explorador possui pelo menos um vértice checkpoint ou não. 
        """
        return len(self.__checks) != 0
    
    def setCheckpoint(self, check: int) -> None:
        """
        Associa o explorador ao valor de um vértice do tipo Checkpoint.\n
        Esse valor é adicionado no início da lista de Checkpoints.
        """
        self.__checks.append(check)

    def getCheckpoint(self) -> int:
        """
        Se existir um valor de vértice Checkpoint esse valor é retornado.\n
        Caso contrário, retorna None.\n
        Em seguida, o Checkpoint é removido da lista de Checkpoints.
        """
        if self.hasCheckpoint():
            return self.__checks.pop()
        return None
    
    def getAttack(self) -> int:
        """
        Retorna o ataque do explorador considerando o dano adicional da arma, se houver.
        """
        attack = super().getAttack()
        if self.hasWeapon():
            attack += self.getWeapon().getDamage()
        return attack
    
    def attack(self) -> tuple[int, str]:
        if self.hasWeapon():
            self.getWeapon().use()
        return super().attack()
    