from models import Weapon

class Espada(Weapon):
    NAME = 'Espada Enferrujada'
    DESCRIPTION = 'Há décadas essa espada vem se desgastando.'
    USABILITY = 6
    DAMAGE = 8
    def __init__(self):
        super().__init__(Espada.NAME, Espada.DESCRIPTION, Espada.USABILITY, Espada.DAMAGE)
        
class Machado(Weapon):
    NAME = 'Machado Velho'
    DESCRIPTION = 'Já não serve para derrubar árvores, talvez sirva em animais inocentes.'
    USABILITY = 4
    DAMAGE = 14
    def __init__(self):
        super().__init__(Machado.NAME, Machado.DESCRIPTION, Machado.USABILITY, Machado.DAMAGE)
        
class Adaga(Weapon):
    NAME = 'Adaga Curta'
    DESCRIPTION = 'Apesar de não ter muito alcance, supreendentemente, está em bom estado.'
    USABILITY = 12
    DAMAGE = 4
    def __init__(self):
        super().__init__(Adaga.NAME, Adaga.DESCRIPTION, Adaga.USABILITY, Adaga.DAMAGE)