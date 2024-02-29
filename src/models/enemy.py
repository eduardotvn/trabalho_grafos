from creature import Creature

class Enemy(Creature):
    
    def __init__(self, hp: int, attack: int):
        super().__init__(hp, attack)
        
