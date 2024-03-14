from models import Explorator
from searches import deepSearch, breadthFirstSearch

class DeepExplorator(Explorator):
    HP = 50
    ATTACK = 6
    NAME = 'Jhonny Deep'
    DESCRIPTION = ''

    def __init__(self) -> None:
        super().__init__(DeepExplorator.HP, DeepExplorator.ATTACK, DeepExplorator.NAME, DeepExplorator.DESCRIPTION)
        self.setSeach(deepSearch)

class BreadthFirstExplorator(Explorator):
    HP = 60
    ATTACK = 5
    NAME = 'Large Paul'
    DESCRIPTION = ''

    def __init__(self) -> None:
        super().__init__(DeepExplorator.HP, DeepExplorator.ATTACK, DeepExplorator.NAME, DeepExplorator.DESCRIPTION)
        self.setSeach(breadthFirstSearch)

