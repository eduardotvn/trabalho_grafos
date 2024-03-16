from models import Explorator, Graph, Enemy
from mobs import Onca, Crocodilo, FormigaQuimera
from random import randint
from .battle import battle

island_creatures = [Onca(), Crocodilo(), FormigaQuimera(), FormigaQuimera(), FormigaQuimera()]

lives = 3

def check_creature_on_node(current_node: int):
    global island_creatures
    for creature in island_creatures:
        if creature.getVertexValue() == current_node:
            return creature
        else:
            continue 
        
def move_creatures(graph: Graph):
    global island_creatures

    for creature in island_creatures:
        if creature.hasVertexValue():
            move_creature(creature, graph)
        else:
            creature.setVertexValue(randint(3, 19))
    
    different_vertex = []
    for creature in island_creatures: 
        if creature.getVertexValue() not in different_vertex:
            different_vertex.append(creature.getVertexValue())
        else: 
            results = battle(creature, island_creatures[different_vertex.index(creature.getVertexValue())])
            if(results.result == "FINISHED"):
                move_creature(results.loser, graph)
            elif(results.result == "MURDERER"): 
                results.loser.resetDeath()
                results.loser.setVertexValue(randint(3, 19))
            

def move_creature(creature, graph: Graph):
        creature_vertex = graph.get(creature.getVertexValue())
        adjacent_list = graph.getAdjacentList(creature_vertex)
        random_vertex = randint(0, len(adjacent_list))
        if random_vertex == len(adjacent_list):
            return
        creature.setVertexValue(adjacent_list[random_vertex].getValue())
        
def ress_explorator(explorator: Explorator):
    if explorator.hasCheckpoint():
        explorator.setVertexValue(explorator.getCheckpoint())
    else: 
        explorator.setVertexValue(0)
    explorator.resetDeath()

def ress_enemy(enemy: Enemy, explorator_pos):
    new_pos = randint(3, 19)
    while new_pos == explorator_pos:
        new_pos = randint(3, 19)
    enemy.resetDeath()
    enemy.setVertexValue(new_pos)

