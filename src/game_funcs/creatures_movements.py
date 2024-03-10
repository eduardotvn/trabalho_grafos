from src.models.graph import *
import random

def check_creature_on_node(current_node: int, creatures: list):
    for creature in creatures:
        return True if creature.get_pos() == current_node else False 
        
def move_creatures(graph: Graph, creatures: list):
    for creature in creatures:
        creature_vertex = graph.get(creature.get_pos())
        adjacent_list = graph.getAdjacentList(creature_vertex)
        random_vertex = random.randint(0, len(adjacent_list))
        if random_vertex == len(adjacent_list):
            continue
        creature.set_pos(adjacent_list[random_vertex])
        
        