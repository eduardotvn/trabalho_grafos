import tkinter as tk
from PIL import Image, ImageTk

vertexes_on_map = [[100, 400], [160, 280], [312, 335], [285, 180], 
                [460, 310], [472, 228], [590, 266], [492, 122], 
                [415, 89], [632, 150], [619, 41], [709, 39],
                [759, 177], [785, 310], [904, 161], [893, 37],
                [1042, 126], [1149, 140], [1203, 37], [1110, 276]]

class Play_Frame:
    def __init__(self, master, image_path, height, width):
        self.master = master
        self.master.title("Treasure Hunt")

        image = Image.open(image_path)
        image = image.resize((width, height))
        photo = ImageTk.PhotoImage(image)

        self.background_image = tk.Label(self.master, image=photo)
        self.background_image.photo = photo
        self.background_image.pack()


