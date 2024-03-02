import tkinter as tk
from src.frames.main_frame import Main_Frame

if __name__ == "__main__":
    height = 720
    width = 1280
    graph = readGraph('grafos/grafo1.txt')
    
    root = tk.Tk()
    app = Main_Frame(root, height=height, width=width)
    root.mainloop()
