import tkinter as tk
from PIL import Image, ImageTk
from src.frames.main_frame import Main_Frame
from src.grafos.read_graph import start_graph

if __name__ == "__main__":
    height = 720
    width = 1280

    root = tk.Tk()
    app = Main_Frame(root, height=height, width=width)
    root.mainloop()
