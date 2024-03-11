from src.models.creature import Creature
from src.models.explorator import Explorator
from random import choice, randint
from math import ceil

class Enemy(Creature):
    """
    Classe de inimigos que podem ser enfrentados pelo jogador.
    """
    def __init__(self, hp: int, attack: int):
        super().__init__(hp, attack)

class FormigaQuimera(Enemy):
    def __init__(self) -> None:
        super().__init__(hp=choice([15, 12, 10]), attack=choice([10, 8, 5]))
        
    def callHelp(self) -> None:
        """
        A cada turno que a formiga não é derrotada ela 'chama' uma parceira, aumentando seu dano em 10%
        e sua vida em 20%
        """
        self.__setAttack(self, (self.getAttack + (.1 * self.getAttack)))
        self.__setHp(self, (self.getHp + (.2 * self.getHp)))

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
        
class Crocodilo(Enemy):
    def __init__(self) -> None:
        super().__init__(hp=choice([40, 30, 20]), attack=choice([20, 15, 10]))
        
    def specialAttack(self) -> tuple[int, str]:
        """
        Lança um dado com chance de 10% de aumentar em 50% o dano do crocodilo.\n
        SA: Special Attack
        """
        damage, strenght = self.attack()
        teste = randint(1, 10)
        if teste == 7:
            damage = damage + ceil(.5 * self.getAttack)
            strenght = 'SA'
        return damage, strenght
        
