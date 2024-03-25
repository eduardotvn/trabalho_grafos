from models import Explorator, Graph, Vertex
from random import choice

def scatter_cpoints(graph: Graph, numChecks: int = 3) -> None:
    """
    Espalha checkpoints pelo grafo.\n
    Se o grafo tem poucos vértices (< 2 * numChecks) nada é feito.
    """
    if graph.getN() < 2 * numChecks: return
    points = []
    vertexs = list(graph.getVertexs())
    while len(points) != numChecks:
        vertex: Vertex = choice(vertexs)
        if not vertex.hasTreasure() and not vertex.isBeginning() and vertex not in points:
            vertex.setCheckPoint()
            points.append(vertex)

def check_point(graph: Graph, value: int, index: int, explorator: Explorator) -> bool:
    """
    Checa se o vértice é local de checkpoint
    """
    from frames.buttons.global_variables import update_checkpoint
    if graph.get(value).isCheckPoint():
        graph.get(value).unSetCheckPoint()
        update_checkpoint(index)
        return True
    return False
    