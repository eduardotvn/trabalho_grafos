from models import Explorator, Graph
import random 

def scatter_cpoints(graph: Graph):
    points = []
    for i in range(3):
        random_point = random.randint(3, 19)
        while random_point in points:
            random_point = random.randint(3, 19)
        print(random_point)
        points.append(random_point)
        graph.get(random_point).setCheckPoint()
        
def check_point(graph: Graph, explorator: Explorator, value: int):
    if graph.get(value).getIsCheckPoint():
        explorator.setCheckpoint(value)
        return True