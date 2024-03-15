from models import Graph, Explorator
from itens import Machado, Adaga, Espada
import random

weapons = [Machado(), Adaga(), Espada(), Espada()]

def set_treasure_vertex(graph: Graph):
    graph.get(19).setTreasure()

def check_treasure_vertex(graph: Graph, explorator: Explorator, value: int):
    treasure_vertex = graph.get(value).getHasTreasure()
    if treasure_vertex:
        explorator.setFoundTreasure()
        return True
    
def scatter_item(graph: Graph):
    vertexes = []
    for i in range(4):
        weapon_vertex = random.randint(1, 19)
        while weapon_vertex in vertexes:
            weapon_vertex = random.randint(1, 19)
        vertexes.append(weapon_vertex)
        graph.get(weapon_vertex).addItem(weapons[i])

def check_for_items(graph: Graph, value: int):
    return graph.get(value).getVertexItens()
