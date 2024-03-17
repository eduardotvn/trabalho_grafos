from models import Explorator, Graph, Enemy, Creature
from entities import Onca, Crocodilo, FormigaQuimera
from random import randint, choice
from .battle import battle

island_creatures = [Onca(), Crocodilo(), FormigaQuimera(), FormigaQuimera(), FormigaQuimera()]

def check_creature_on_node(current_node: int):
    """
    Checa se há criaturas no mesmo nodo do jogador
    """
    global island_creatures
    for creature in island_creatures:
        if creature.getVertexValue() == current_node:
            return creature
        else:
            continue 
        
def chooseVertex(graph: Graph) -> int:
    """
    Escolhe um vértice do grafo elegível para o spawn de criaturas.
    """
    vertexs = list(graph.getVertexs())
    vertex = choice(vertexs)
    while vertex.isBeginning() or vertex.isCheckPoint():
        vertex = choice(vertexs)
    return vertex.getValue()

def move_creatures(graph: Graph):
    """
    Faz as criaturas se moverem pelo grafo\n
    iterando seu vetor de objetos
    """
    global island_creatures

    for creature in island_creatures:
        if creature.hasVertexValue():
            move_creature(creature, graph)
        else:
            creature.setVertexValue(chooseVertex(graph))
    
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
            
def move_creature(creature: Creature, graph: Graph):
    """
    Move uma criatura pelo grafo.
    """
    creature_vertex = graph.get(creature.getVertexValue())
    adjacent_list = graph.getAdjacentList(creature_vertex).copy() # Cópia da lista de adjacência
    adjacent_list.append(creature_vertex) # A criatura pode escolher ficar no seu vértice atual
    for vertex in adjacent_list:
        if vertex.isCheckPoint() or vertex.isBeginning():
            adjacent_list.remove(vertex)
    random_vertex = choice(adjacent_list)
    creature.setVertexValue(random_vertex.getValue())
        
def ress_explorator(explorator: Explorator):
    """
    Ressuscita o explorador.
    """
    if explorator.hasCheckpoint():
        explorator.setVertexValue(explorator.getCheckpoint())
    else: 
        explorator.setVertexValue(0)
    explorator.resetDeath()

def ress_enemy(enemy: Enemy, explorator_pos):
    """
    Ressuscita uma criatura
    """
    new_pos = randint(3, 19)
    while new_pos == explorator_pos:
        new_pos = randint(3, 19)
    enemy.resetDeath()
    enemy.setVertexValue(new_pos)

