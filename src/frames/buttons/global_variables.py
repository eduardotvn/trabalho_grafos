from models import readGraph
from entities import DeepExplorator, BreadthFirstExplorator

graph = readGraph('grafos/grafo1.txt')
player = DeepExplorator()

path = player.getSeach(graph, graph.get(0))
index = 0
checkpoint_index = 0
current_pos = path[index] 
current_vertex = graph.get(current_pos)
menu_pos = [360, 380]

def update_index(value):
    """
    Atualiza o valor da variável global index
    """
    global index
    index = value 

def update_checkpoint(value):
    global checkpoint_index
    checkpoint_index = value

def update_current_pos():
    """
    Atualiza o valor da variável global current_pos e current_vertex\n
    pois são relacionadas.
    """
    global index, current_pos
    current_pos = path[index]
    update_current_vertex()

def update_current_vertex():
    """
    Atualiza o valor da variável global current_vertex
    """
    global current_pos, current_vertex
    current_vertex = graph.get(current_pos)

def reset_graph():
    """
    Reseta o grafo para recomeçar o jogo
    """
    global graph 
    graph = readGraph('grafos/grafo1.txt')

def reset_player(value):
    """
    Reseta o player para recomeçar o jogo
    """
    global player
    if value == 1:
        player = DeepExplorator()
    else:
        player = BreadthFirstExplorator()

def reset_path():
    """
    Reseta o caminho para recomeçar o jogo
    """
    global player, path
    path = player.getSeach(graph, graph.get(0))

def get_index():
    """
    Retorna o valor da variável global index
    """
    global index
    return index

def get_checkpoint_index():
    global checkpoint_index
    return checkpoint_index

def get_current_pos():
    """
    Retorna o valor da variável global current_pos
    """
    global current_pos
    return current_pos

def get_current_vertex():
    """
    Retorna o valor da variável global current_vertex
    """
    global current_vertex
    return current_vertex

def get_path():
    """
    Retorna o valor da variável global path
    """
    global path
    return path

def get_graph():
    """
    Retorna o valor da variável global graph
    """
    global graph
    return graph

def get_player():
    """
    Retorna o valor da variável global player
    """
    global player
    return player
