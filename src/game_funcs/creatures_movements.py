from src.models.graph import *
import random
from src.models.enemy import *
from src.game_funcs.battle import *
from src.models.creature import Creature
from src.models.explorator import Explorator

island_creatures = [Onca(), Crocodilo(), FormigaQuimera(), FormigaQuimera(), FormigaQuimera()]

lives = 3

def check_creature_on_node(current_node: int):
    global island_creatures
    for creature in island_creatures:
        print("Criatura " + creature.__class__.__name__ +" no vertice " + str(creature.getVertexValue()))
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
            creature.setVertexValue(random.randint(3, 19))
    
    different_vertex = []
    for creature in island_creatures: 
        if creature.getVertexValue() not in different_vertex:
            print(different_vertex)
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
        random_vertex = random.randint(0, len(adjacent_list))
        if random_vertex == len(adjacent_list):
            return
        creature.setVertexValue(adjacent_list[random_vertex].getValue())
        
def ress_explorator(explorator: Explorator):
    if explorator.hasCheckpoint():
        explorator.setVertexValue(explorator.getCheckpoint())
    else: 
        explorator.setVertexValue(0)