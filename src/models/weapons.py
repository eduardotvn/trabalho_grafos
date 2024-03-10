from src.models.item import Weapon

class Espada(Weapon):
    NAME = 'Espada Enferrujada'
    DESCRIPTION = 'Há décadas essa espada vem se desgastando'
    USABILITY = 3
    DAMAGE = 7
    def __init__(self):
        super().__init__(Espada.NAME, Espada.DESCRIPTION, Espada.USABILITY, Espada.DAMAGE)
        
class Machado(Weapon):
    NAME = 'Machado Velho'
    DESCRIPTION = 'Já não serve para derrubar árvores, talvez sirva em animais inocentes.'
    USABILITY = 2
    DAMAGE = 10
    def __init__(self):
        super().__init__(Machado.NAME, Machado.DESCRIPTION, Machado.USABILITY, Machado.DAMAGE)
        
class Adaga(Weapon):
    NAME = 'Adaga Curta'
    DESCRIPTION = 'Apesar de não ter muito alcance, supreendentemente, está em bom estado'
    USABILITY = 7
    DAMAGE = 4
    def __init__(self):
        super().__init__(usability=3, damage=3)