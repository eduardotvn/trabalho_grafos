from entities.traps import PlantaCarnivora, AreiaMovedica, CaminhoIngreme
import random
from models.graph import Graph
from .scatter_checkpoints import check_point

traps = [PlantaCarnivora(), AreiaMovedica(), CaminhoIngreme(), CaminhoIngreme()]

def scatter_traps_func(graph: Graph): 
    global traps
    vertexes = [] 
    for trap in traps:
        random_pos = random.randint(3, 19)
        while random_pos in vertexes or graph.get(random_pos).isCheckPoint():
            random_pos = random.randint(3, 19)
        graph.get(random_pos).setTrap(trap)
        vertexes.append(random_pos)

def check_for_traps(graph: Graph, value: int):
    if graph.get(value).hasTrap():
        return graph.get(value).getTrap()