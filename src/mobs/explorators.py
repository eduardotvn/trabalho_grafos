from models import Explorator
from searches import deepSearch, breadthFirstSearch

class DeepExplorator(Explorator):
    HP = 50
    ATTACK = 5
    NAME = 'Jhonny Deep'
    DESCRIPTION = 'Jhonny sempre vai vundo para achar o que procura'

    def __init__(self) -> None:
        super().__init__(DeepExplorator.HP, DeepExplorator.ATTACK, DeepExplorator.NAME, DeepExplorator.DESCRIPTION)
        self.setSeach(deepSearch)

class BreadthFirstExplorator(Explorator):
    HP = 60
    ATTACK = 7
    NAME = 'Large Paul'
    DESCRIPTION = 'Paul sempre prefere checar todas as opções antes de seguir em frente'

    def __init__(self) -> None:
        super().__init__(DeepExplorator.HP, DeepExplorator.ATTACK, DeepExplorator.NAME, DeepExplorator.DESCRIPTION)
        self.setSeach(breadthFirstSearch)
