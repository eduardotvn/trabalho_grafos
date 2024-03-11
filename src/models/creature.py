from random import choice, randint
from math import ceil

class Creature():
    
    def __init__(self, hp: int, attack: int) -> None:
        self.__hp = hp
        self.__HP_MAX = hp
        self.__attack = attack
        self.__vertexValue: int = None

    def getAttack(self) -> int:
        """
        Retorna o ataque da criatura.
        """
        return self.__attack
    
    def getHp(self) -> int:
        """
        Retorna o HP da criatura.
        """
        return self.__hp

    def getMaxHp(self) -> int:
        """
        Retorna o HP máximo permitido para a criatura.
        """
        return self.__HP_MAX
    
    def hasVertexValue(self) -> bool:
        """
        Retorna se a criatura possui um valor de vértice definido.
        """
        return self.__vertexValue != None
    
    def getVertexValue(self) -> int | None:
        """
        Retorna o valor do vértice no qual a criatura está.
        """
        return self.__position
    
    def setVertexValue(self, value: int) -> None:
        """
        Altera a posição da criatura no grafo para o valor do vértice passado.
        """
        self.__position = value

    def __setHp(self, hp: int) -> None:
        """
        NÃO DEVE SER USADO.\n
        Altera o HP da criatura. \n
        Desde que o HP seja maior ou igual a zero e menor que o HP máximo.
        """
        if hp >= 0 and hp <= self.__HP_MAX:
            self.__hp = hp

    def fullHealth(self) -> None:
        """
        Altera o HP da criatura para o seu valor máximo.
        """
        self.__setHp(self.__HP_MAX)

    def setDamage(self, damage: int) -> None:
        """
        Reduz o HP da criatura, desde que o dano seja positivo.\n
        Se o dano for maior que o HP então a criatura ficará com zero de HP.
        """
        if damage <= 0:
            return
        if damage > self.getHp():
            damage = self.getHp()
        self.__setHp(self.getHp() - damage)
    
    def setHeal(self, heal: int) -> None:
        """
        Aumenta o HP da criatura, desde que o aumento seja positivo.\n
        Se o aumento somado ao HP atual for maior que o HP máximo então a criatura ficará com a vida cheia.
        """
        if heal <= 0:
            return
        if heal + self.getHp() > self.__HP_MAX:
            self.__setHp(self.__HP_MAX)
        self.__setHp(self.getHp() + heal)
    
    def isDead(self) -> bool:
        """
        Retorna Verdadeiro se a criatura estiver morta, Falso caso contrário.
        """
        return self.getHp() == 0
    
    def isAlive(self) -> bool:
        """
        Retorna Verdadeiro se a criatura estiver viva, Falso caso contrário.
        """
        return not self.isDead()
    
    def attack(self) -> tuple[int, str]:
        """
        Retorna o valor do dano gerado pelo ataque e sua força ('W', 'M' ou 'S').\n
        Tando a força do ataque quando o dano são escolhidos aleatoriamente.\n
        W - Fraco (20%)\n
        M - Médio (60%)\n
        S - Forte (20%)\n
        """
        strength = choice(['W', 'M', 'M', 'M', 'S'])

        if strength == 'W':
            damage = randint(1, ceil(.3 * self.getAttack()))
        elif strength == 'M':
            damage = randint(ceil(.4 * self.getAttack()), ceil(.6 * self.getAttack()))
        else:
            damage = randint(ceil(.7 * self.getAttack()), self.getAttack())
        
        return damage, strength
    
    def getHitFrom(self, creature) -> tuple[int, str]:
        """
        Atribui o dano de ataque da criatura passada, se ela estiver viva, a criatura.
        """
        if creature.isAlive():
            damage, strength = creature.attack()
            self.setDamage(damage)
            return damage, strength
        return 0, 'W'

    def resetDeath(self) -> None:
        """
        Pode ser usado quando uma criatura está morta. \n
        Esta função traz a criatura de volta a vida!
        """
        if self.isDead():
            self.fullHealth()

    def __repr__(self) -> str:
        return f'Creature(hp={self.__hp}, attack={self.__attack}, HP_MAX={self.__HP_MAX})'
