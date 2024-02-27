

class Creature:
    
    def __init__(self, hp: int, attack: int) -> None:
        self.__hp = hp
        self.__attack = attack

    def getAttack(self) -> int:
        return self.__attack

    def setAttack(self, attack: int) -> None:
        if attack <= 0:
            return
        self.__attack = attack
    
    def getHp(self) -> int:
        return self.__hp

    def setHp(self, hp: int) -> None:
        if hp < 0:
            return
        self.__hp = hp

    def setDamage(self, damage: int) -> None:
        if (damage > self.getHp()):
            damage = self.getHp()
        self.setHp(self.getHp() - damage)
    
    def isDead(self) -> bool:
        return self.getHp() == 0
    
    def isAlive(self) -> bool:
        return not self.isDead()
    
def fight(c1: Creature, c2: Creature):
    pass
