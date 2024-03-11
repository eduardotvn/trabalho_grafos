from src.models.graph import *
import random
from src.models.enemy import *

island_creatures = [Onca(), Crocodilo(), FormigaQuimera(), FormigaQuimera(), FormigaQuimera()]

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
            continue
        else:
            creature.setVertexValue(random.randint(3, 19))

    for creature in island_creatures:
        creature_vertex = graph.get(creature.getVertexValue())
        adjacent_list = graph.getAdjacentList(creature_vertex)
        random_vertex = random.randint(0, len(adjacent_list))
        if random_vertex == len(adjacent_list):
            continue
        creature.setVertexValue(adjacent_list[random_vertex].getValue())
            