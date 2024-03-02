import tkinter as tk
from src.frames.main_frame import Main_Frame
from src.models.graph import Graph, Vertex

def readGraph() -> Graph:
    graph = Graph(directional=False)
    with open('grafos/grafo1.txt') as graphText:
        for line in graphText.readlines():
            line = line.strip().split(':')
            vertex = Vertex(int(line.pop(0)))
            graph.addVertex(vertex)
            
            vertexEdges = line.pop(0).strip().split(' ')
            for edge in vertexEdges:
                neighbor = Vertex(int(edge))
                graph.addEdge(vertex, neighbor)
    return graph


if __name__ == "__main__":
    height = 720
    width = 1280
    graph = readGraph()

    root = tk.Tk()
    app = Main_Frame(root, height=height, width=width)
    root.mainloop()
