import tkinter as tk
from src.frames.main_frame import Main_Frame
from src.models.graph import readGraph
from src.models.explorator import Explorator
from src.models.search import deepSearch

if __name__ == "__main__":
    height = 720
    width = 1280

    root = tk.Tk()
    app = Main_Frame(root, height=height, width=width)

    root.mainloop()

    
