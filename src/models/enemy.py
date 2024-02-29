from creature import Creature

class Enemy(Creature):
    
    def __init__(self, hp: int, attack: int):
        super().__init__(hp, attack)

    def resetDeath(self) -> None:
        """
        Pode ser usado quando uma criatura está morta. \n
        Esta função traz a criatura de volta a vida!
        """
        if self.isDead():
            self.fullHealth()

