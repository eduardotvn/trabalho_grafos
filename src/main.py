import tkinter as tk
from frames import Main_Frame

if __name__ == "__main__":
    height = 720
    width = 1280

    root = tk.Tk()
    app = Main_Frame(root, height=height, width=width)

    root.mainloop()

    
