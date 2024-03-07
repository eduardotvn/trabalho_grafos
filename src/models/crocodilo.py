from enemy import Enemy
from random import choice, randint
from math import ceil

class Crocodilo(Enemy):
    def __init__(self) -> None:
        super.__init__(hp=choice([40, 30, 20]), attack=choice([20, 15, 10]))
        
    def specialAttack(self) -> tuple[int, str]:
        damage, strenght = self.attack()
        "Lança um dado com chance de 10% de aumentar em 50% o dano do crocodilo"
        teste = randint(1, 10)
        if teste == 7:
            damage = damage + ceil(.5 * self.getAttack)
            """
            SA: Special Attack
            """
            strenght = 'SA'
        return damage, strenght
        