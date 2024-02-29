from creature import Creature

class Explorator(Creature):

    def __init__(self, hp: int, attack: int):
        self.pocket = None
        self.hand = None
        super().__init__(hp, attack)
