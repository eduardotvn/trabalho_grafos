from enemy import Enemy
from random import choice

class FormigaQuimera(Enemy):
    def __init__(self) -> None:
        super().__init__(hp=choice([15, 12, 10]), attack=choice([10, 8, 5]))
        
    def callHelp(self) -> None:
        """
        A cada turno que a formiga não é derrotada ela 'chama' uma parceira, aumentando seu dano em 10%
        e sua vida em 20%
        """
        self.__setAttack(self, (self.getAttack + (.1 * self.getAttack)))
        self.__setHp(self, (self.getHp + (.2 * self.getHp)))