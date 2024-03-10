from src.models.creature import Creature
from src.models.explorator import Explorator
from src.models.enemy import Enemy
from dataclasses import dataclass, field
from enum import Enum

class BattleResult(Enum):
    FINISHED = 0
    DIED = 1
    MURDERER = 2

@dataclass(frozen=True)
class Battle():
    """
    Classe de dados para batalhas.\n
    \ttype: tipo da batalha\n
    \tresultId: cada id representa um resultado de batalha diferente\n
    \tresult: uma string que representa um dos resultados possíveis da batalha\n
    \texploratorDamage: tupla contento o dano e força do ataque do explorador. Apenas em: Explorador x Inimigo\n 
    \tenemyDamage: tupla contento o dano e força do ataque do inimigo. Apenas em: Explorador x Inimigo\n
    \twinner: vencedor da batalha do tipo Inimigo x Inimigo\n
    \tloser: perdedor da batalha do tipo Inimigo x Inimigo\n
    """
    type: str
    resultId: int
    result: str
    exploratorDamage: tuple[int, str] = field(default_factory=tuple)
    enemyDamage: tuple[int, str] = field(default_factory=tuple)
    winner: Creature = field(default_factory=Creature)
    loser: Creature = field(default_factory=Creature)

def battle(creature1: Creature, creature2: Creature) -> Battle:
    """
    Função de batalha, passando como arguemento duas criaturas, essas irão lutar.
    """
    if isinstance(creature1, Enemy) and isinstance(creature2, Enemy):
        return enemiesBattle(creature1, creature2)
    elif isinstance(creature1, Explorator) and isinstance(creature2, Enemy):
        return exploratorBattle(creature1, creature2)
    elif isinstance(creature2, Explorator) and isinstance(creature1, Enemy):
        return exploratorBattle(creature2, creature1)

def exploratorBattle(explorator: Explorator, enemy: Enemy) -> Battle:
    """
    Batalha entre um explorador e uma inimigo.
    """
    enemyDamage = explorator.getHitFrom(enemy)
    exploratorDamage = enemy.getHitFrom(explorator)

    result = calcResultBattle(explorator, enemy)
    return Battle('Explorator x Enemy', result.value, result.name, exploratorDamage, enemyDamage, None, None)

def enemiesBattle(enemy1: Enemy, enemy2: Enemy) -> Battle:
    winner, loser = enemy1, enemy2
    if enemy1.getAttack() > enemy2.getAttack():
        enemy2.getHitFrom(enemy1)
    else:
        enemy1.getHitFrom(enemy2)
        winner, loser = loser, winner

    result = calcResultBattle(winner, loser)
    return Battle('Enemy x Enemy', result.value, result.name, None, None, winner, loser)
    
def calcResultBattle(winner: Enemy, loser: Enemy) -> BattleResult:
    if winner.isAlive() and loser.isAlive():
        return BattleResult.FINISHED
    elif winner.isAlive() and loser.isDead():
        return BattleResult.MURDERER
    elif winner.isDead() and loser.isAlive():
        return BattleResult.DIED
