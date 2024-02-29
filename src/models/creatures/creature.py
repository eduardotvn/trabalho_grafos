from models.graph.graph import Vertex
from random import choice

class Creature:
    
    def __init__(self, hp: int, attack: int, vertexValue: int) -> None:
        self.__hp = hp
        self.__HP_MAX = hp
        self.__attack = attack
        self.__vertexValue = vertexValue

    def getAttack(self) -> int:
        """
        Retorna o ataque da criatura.
        """
        return self.__attack

    def setAttack(self, attack: int) -> None:
        """
        Altera o ataque da criatura.\n
        Desde que o valor passado seja maior que zero.
        """
        if attack <= 0:
            return
        self.__attack = attack
    
    def getHp(self) -> int:
        """
        Retorna o HP da criatura.
        """
        return self.__hp

    def __setHp(self, hp: int) -> None:
        """
        Altera o HP da criatura. \n
        Desde que o HP seja maior ou igual a zero.
        """
        if hp < 0:
            return
        self.__hp = hp

    def setDamage(self, damage: int) -> None:
        """
        Reduz o HP da criatura.\n
        Desde que o dano seja positivo.\n
        Se o dano for maior que o HP então a criatura ficará com zero de HP.
        """
        if damage <= 0:
            return
        if damage > self.getHp():
            damage = self.getHp()
        self.__setHp(self.getHp() - damage)
    
    def setHeal(self, heal: int) -> None:
        """
        Aumenta o HP da criatura.\n
        Desde que o aumento seja positivo.\n
        Se o aumento mais o HP atual for maior que o HP máximo então a criatura ficará com a vida cheia.
        """
        if heal <= 0:
            return
        if heal + self.getHp() > self.__HP_MAX:
            self.__setHp(self.__HP_MAX)
        self.__setHp(self.getHp() + heal)
    
    def isDead(self) -> bool:
        """
        Retorna True se a criatura estiver morta.
        """
        return self.getHp() == 0
    
    def isAlive(self) -> bool:
        """
        Retorna True se a criatura estiver viva.
        """
        return not self.isDead()
    
    def getVertexValue(self) -> int:
        """
        Retorna o valor único do vértice onde a criatura está.
        """
        return self.__vertexValue
    
    def move(self, adjacencyList: list[Vertex]) -> Vertex:
        """
        Move a criatura para um novo vértice escolhido aleatoriamente. \n
        Retorna o vértice escolhido.
        """
        v = choice(adjacencyList)
        self.__vertexValue = v.getValue()
        return v
