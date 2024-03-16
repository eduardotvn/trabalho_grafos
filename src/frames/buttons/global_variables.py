from models import readGraph
from mobs import DeepExplorator, BreadthFirstExplorator

graph = readGraph('grafos/grafo1.txt')
player = DeepExplorator()

path = player.getSeach(graph, graph.get(0))
index = 0
current_pos = path[index] 
current_vertex = graph.get(current_pos)
menu_pos = [360, 380]

def update_index(value):
    global index
    index = value 

def update_current_pos():
    global index, current_pos
    current_pos = path[index]
    update_current_vertex()

def update_current_vertex():
    global current_pos, current_vertex
    current_vertex = graph.get(current_pos)

def reset_graph():
    global graph 
    graph = readGraph('grafos/grafo1.txt')

def reset_player(value):
    global player
    if value == 1:
        player = DeepExplorator()
    else:
        player = BreadthFirstExplorator()

def reset_path():
    global player, path
    path = player.getSeach(graph, graph.get(0))

def get_index():
    global index
    return index

def get_current_pos():
    global current_pos
    return current_pos

def get_current_vertex():
    global current_vertex
    return current_vertex

def get_path():
    global path
    return path

def get_graph():
    global graph
    return graph

def get_player():
    global player
    return player
