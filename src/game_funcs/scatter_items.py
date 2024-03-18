from models import Graph, Explorator
from entities import Machado, Adaga, Espada
from entities.itens.cures import PingoDaLua, PomosDeOuro, CogumeloAngelical
import random

weapons = [Machado(), Adaga(), Espada(), Espada()]
cures = [CogumeloAngelical(), CogumeloAngelical(), PingoDaLua(), PomosDeOuro()]

def set_treasure_vertex(graph: Graph):
    graph.get(19).setTreasure()

def check_treasure_vertex(graph: Graph, explorator: Explorator, value: int):
    treasure_vertex = graph.get(value).hasTreasure()
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
    vertexes = []
    for i in range(4):
        cure_vertex = random.randint(1, 19)
        while cure_vertex in vertexes:
            cure_vertex = random.randint(1, 19)
        vertexes.append(cure_vertex)
        graph.get(cure_vertex).addItem(cures[i])
    
def check_for_items(graph: Graph, value: int):
    return graph.get(value).getVertexItens()
