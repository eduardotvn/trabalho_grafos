from enemy import Enemy
from explorator import Explorator
from random import choice
from math import ceil

class Onca(Enemy):
    def __init__(self) -> None:
        super().__init__(hp=choice([25, 20, 15]), attack=choice([15, 12, 10]))
        
    def quickDodge(self, explorator: Explorator) -> tuple[int, str, str]:
        damage, strength = explorator.attack();
        """
        A onça pode desviar do ataque do explorador sendo as porcentagens:
        F - Falhar (50%) Onça recebe 100% do dano do ataque
        D - Desvio (40%) Onça recebe 50% do dano do ataque
        P - Perfeito (10%) Onça não recebe dano
        """
        dodge = choice(['F', 'F', 'F', 'F', 'F', 'F', 'D', 'D', 'D', 'D','P'])
        
        if dodge == 'F':
            return damage, strength, dodge
        elif dodge == 'D':
            damage = ceil(.5 * damage)
            return damage, strength, dodge
        else:
            damage = 0
            return damage, strength, dodge
        