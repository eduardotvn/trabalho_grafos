from entities import PlantaCarnivora, AreiaMovedica, CaminhoIngreme
from random import choice
from models import Graph, Vertex, Trap

traps = [PlantaCarnivora(), AreiaMovedica(), CaminhoIngreme(), CaminhoIngreme()]

def scatter_traps_func(graph: Graph) -> None: 
    global traps
    if len(traps) > graph.getN() - 1:
        raise Exception('Muitas armadilhas para poucos vértices')
    vertexs = list(graph.getVertexs())
    for trap in traps:
        randomVertex: Vertex = choice(vertexs)
        while randomVertex.isCheckPoint() or randomVertex.isBeginning():
            randomVertex = choice(vertexs)
        randomVertex.setTrap(trap)

def check_for_traps(graph: Graph, value: int) -> Trap | None:
    if graph.get(value).hasTrap():
        return graph.get(value).getTrap()