from random import choice, randint
from math import ceil
from models import Enemy, Explorator
 
class FormigaQuimera(Enemy):
    NAME = 'Formiga Quimera'
    DESCRIPTION = 'São formigas destemidas e unidas, irritar uma é irritar todas.'
    __IN_RAGE = False

    def __init__(self) -> None:
        super().__init__(hp=choice([15, 12, 10]), attack=choice([10, 8, 6]), name=FormigaQuimera.NAME, description=FormigaQuimera.DESCRIPTION)
    
    def attack(self) -> tuple[int, str]:
        damage, strength = super().attack()
        if FormigaQuimera.__IN_RAGE:
            damage += int(damage * .20)
        return damage, strength
    
    def getHitFrom(self, creature) -> tuple[int, str]:
        """
        Atribui o dano de ataque da criatura passada, se ela estiver viva.\n
        Existe uma chance de 60% da formiga quimera charmar ajuda.\n
        Neste caso, todas elas terão aumento de 20% de dano.
        """
        if randint(1, 10) > 6:
            FormigaQuimera.__IN_RAGE = True
        return super().getHitFrom(creature)

class Onca(Enemy):
    NAME = 'Onça Mítica'
    DESCRIPTION = 'Extremamente rápidas e agressivas, sua velocidade as torna um alvo difícil.'

    def __init__(self) -> None:
        super().__init__(hp=choice([25, 20, 15]), attack=choice([15, 12, 10]), name=Onca.NAME, description=Onca.DESCRIPTION)

    def getHitFrom(self, creature) -> tuple[int, str]:
        if isinstance(creature, Enemy):
            return super().getHitFrom(creature)
        elif isinstance(creature, Explorator):
            damage, strength = creature.attack()
            damage = self.quickDodge(damage)
            self.setDamage(damage)
            return damage, strength
        
    def quickDodge(self, damage: int) -> int:
        """
        A onça pode desviar do ataque do explorador sendo as porcentagens:\n
        F - Falhar (70%) Onça recebe 100% do dano do ataque\n
        D - Desvio (20%) Onça recebe 50% do dano do ataque\n
        P - Perfeito (10%) Onça não recebe dano
        """
        dodge = choice(['F', 'F', 'F', 'F', 'F', 'F', 'F', 'D', 'D', 'P'])
        
        if dodge == 'F':
            return damage
        elif dodge == 'D':
            return ceil(.5 * damage)
        else:
            return 0
        
class Crocodilo(Enemy):
    NAME = 'Crocodilo Colossal'
    DESCRIPTION = 'Poucas coisas doem mais que uma mordida certeira desses crocodilos.'

    def __init__(self) -> None:
        super().__init__(hp=choice([27, 25, 20]), attack=choice([20, 15, 12]), name=Crocodilo.NAME, description=Crocodilo.DESCRIPTION)
        
    def attack(self) -> tuple[int, str]:
        """
        Retorna o valor do dano gerado pelo ataque e sua força ('W', 'M' ou 'S').\n
        Tando a força do ataque quando o dano são escolhidos aleatoriamente.\n
        W - Fraco (20%)\n
        M - Médio (60%)\n
        S - Forte (20%)\n
        Adicionalmente o Crocodilo pode lançar um ataque especial (10%).\n
        Caso isso ocorra o dado gerado é aumentado em 50%.\n
        E na força é adicionado o sufixo "S".\n
        WS - Fraco especial\n
        MS - Médio especial\n
        SS - Forte especial 
        """
        damage, strength = super().attack()
        if randint(1, 10) == 5:
            damage += ceil(damage * .5)
        return damage, strength + 'S'
        