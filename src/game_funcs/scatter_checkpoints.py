from models import Explorator, Graph
import random 

def scatter_cpoints(graph: Graph):
    """
    Espalha checkpoints pelo grafo
    """
    points = []
    for i in range(3):
        random_point = random.randint(3, 19)
        while random_point in points:
            random_point = random.randint(3, 19)
        print(random_point)
        points.append(random_point)
        graph.get(random_point).setCheckPoint()
    
def check_point(graph: Graph, value: int, index: int, explorator: Explorator):
    """
    Checa se o vértice é local de checkpoint
    """
    from frames.buttons.global_variables import update_checkpoint
    if graph.get(value).getIsCheckPoint():
        if explorator.hasCheckpoint():
            explorator.getCheckpoint()
        graph.get(value).unCheckPoint()
        update_checkpoint(index)
        return True
    