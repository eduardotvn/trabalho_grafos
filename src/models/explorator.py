from .creature import Creature
from .weapon import Weapon
from .graph import Graph, Vertex
from typing import Callable

class Explorator(Creature):

    TREASURE_CAPACITY = 100

    def __init__(self, hp: int, attack: int, name: str, description: str) -> None:
        super().__init__(hp, attack, name, description)
        self.__weapon: Weapon = None
        self.__checks: list = []
        self.__treasurePocket: int = 0
        self.__lives: int = 3
        self.__search: Callable[[Graph, Vertex], list[int]] = None
    
    def setSeach(self, search: Callable[[Graph, Vertex], list[int]]) -> None:
        self.__search = search
    
    def getSeach(self, graph: Graph, vertex: Vertex) -> list[int]:
        return self.__search(graph, vertex)

    def getLives(self) -> int:
        return self.__lives

    def discountLife(self):
        if self.__lives > 0:
            self.__lives -= 1

    def attack(self) -> tuple[int, str]:
        if self.hasWeapon():
            self.getWeapon().use()
        return super().attack()
    
    def discartWeapon(self) -> Weapon | None:
        """
        Faz o explorador discartar a arma que antes segurava.\n
        Retorna a arma usada, caso exista.
        """
        return self.setWeapon(None)
    
    def __updateTreasure(self) -> None:
        """
        Atualiza a quantidade de tesouro carregado.
        """
        if self.hasTreasure():
            self.__setTreasurePocket(self.__calcTreasureCapacity())

    def hasTreasure(self) -> bool:
        """
        Retorna Verdade se o explorador está carregando algum tesouro. 
        """
        return self.__treasurePocket != 0

    def hasWeapon(self) -> bool:
        """
        Retorna se o explorador está ou não segurando uma arma.
        """
        return self.__weapon != None
    
    def hasCheckpoint(self) -> bool:
        """
        Retorna se o explorador possui pelo menos um vértice checkpoint ou não. 
        """
        return bool(self.__checks)

    def getCheckpoint(self) -> int | None:
        """
        Se existir um valor de vértice Checkpoint esse valor é retornado.\n
        Caso contrário, retorna None.\n
        Em seguida, o Checkpoint é removido da lista de Checkpoints.
        """
        if self.hasCheckpoint():
            return self.__checks.pop()
        return None
    
    def getAttack(self) -> int:
        """
        Retorna o ataque do explorador. \n
        Adciona o dano adicional da arma segurada, se houver.
        """
        attack = super().getAttack()
        if self.hasWeapon():
            attack += self.getWeapon().getDamage()
        return attack
    
    def getWeapon(self) -> Weapon | None:
        """
        Retorna a arma segurada pelo explorador caso ela exista.
        """
        return self.__weapon
    
    def getTreasurePocket(self) -> int:
        """
        Retorna a quantidade de tesouro que o explorador está carregando.
        """
        return self.__treasurePocket
    
    def setWeapon(self, weapon: Weapon) -> Weapon | None:
        """
        Altera a arma segurada pelo explorador para a arma passada. \n
        Retorna a arma segurada antes pelo explorador, caso exista.
        """
        oldWeapon = self.getWeapon()    
        self.__weapon = weapon
        if weapon: self.__updateTreasure()
        return oldWeapon
    
    def setCheckpoint(self, check: int) -> None:
        """
        Associa o explorador ao valor de um vértice do tipo Checkpoint.\n
        Esse valor é adicionado no início da lista de Checkpoints.
        """
        self.__checks.append(check)

    def __setTreasurePocket(self, treasure: int) -> None:
        """
        Altera o valor do tesouro carregado pelo explorador.
        """
        if treasure > 0:
            self.__treasurePocket = treasure
        else:
            self.__treasurePocket = 0

    def setDamage(self, damage: int) -> int:
        super().setDamage(damage)
        self.__updateTreasure()
        return damage

    def setFoundTreasure(self) -> None:
        """
        Deve ser chamada quando o explorador acha o tesouro.\n
        Essa função atribui a ``treasurePocket`` a quantidade de tesouso que pode ser carregada.\n
        Leva em consideração o HP restante e a arma segurada pelo explorador.
        """
        # porcentagem de HP restante
        self.__setTreasurePocket(self.__calcTreasureCapacity())
    
    def __calcTreasureCapacity(self) -> int:
        """
        Calcula a quantidade de tesouro que pode ser carragada pelo explorador.
        """
        # porcentagem de HP restante
        remainingHP: float = (1 - (self.getMaxHp() - self.getHp()) / self.getMaxHp())
        capacity: int = int(Explorator.TREASURE_CAPACITY * remainingHP)
        if self.hasWeapon():
            capacity -= self.getWeapon().getDamage()
        return capacity

    def __repr__(self) -> str:
        if self.hasWeapon():
            return f'Explorator(hp={self.getHp()}, attack={self.getAttack()}, weapon={self.getWeapon().tostring()}, treasurePocket={self.getTreasurePocket()}, HP_MAX={self.getMaxHp()})'
        return f'Explorator(hp={self.getHp()}, attack={self.getAttack()}, treasurePocket={self.getTreasurePocket()}, HP_MAX={self.getMaxHp()})'
    