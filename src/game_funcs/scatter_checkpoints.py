from src.models.graph import Graph, Vertex
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
