from item import Weapon

class Espada(Weapon):
    def __init__(self):
        super().__init__(usability=3, damage=5)
        
class Machado(Weapon):
    def __init__(self):
        super().__init__(usability=3, damage=8)
        
class Adaga(Weapon):
    def __init__(self):
        super().__init__(usability=3, damage=3)