import tkinter as tk
from PIL import Image, ImageTk
from tkinter import PhotoImage
from src.models.search import *
from src.models.graph import *
from src.models.explorator import *
from tkinter import font


vertexes_on_map = [[100, 400], [312, 335], [160, 280], [285, 180], 
                [460, 310], [472, 228], [590, 266], [492, 122], 
                [415, 89], [632, 150], [619, 41], [709, 39],
                [759, 177], [785, 310], [904, 161], [893, 37],
                [1042, 126], [1110, 276], [1149, 140], [1203, 37]]

graph = readGraph('grafos/grafo1.txt')
player = Explorator(50, 5)
path = deepSearch(graph, graph.get(0))
index = 0
current_pos = path[index] 
current_vertex = graph.get(current_pos)
creature_on_vertex = False
clear_area_options = ["Procurar por recursos"]
fight_options = ["Lutar", "Fugir"]
menu_pos = [360, 380]

class Play_Frame:
    def __init__(self, master, image_path, height, width):
        self.master = master
        self.master.title("Treasure Hunt")

        custom_font = font.Font(family="Gabriola", size=24)
        image = Image.open(image_path)
        image = image.resize((width, height))
        photo = ImageTk.PhotoImage(image)

        self.background_image = tk.Label(self.master, image=photo, bd=0)
        self.background_image.photo = photo
        self.background_image.pack()

        self.menu_bar_image = Image.open("assets/menu/menu_bar.png")
        self.menu_bar_image = self.menu_bar_image.resize((720, 320))
        menu_bar_photo = ImageTk.PhotoImage(self.menu_bar_image)

        self.menu_bar_label = tk.Label(self.master, image=menu_bar_photo)
        self.menu_bar_label.photo = menu_bar_photo
        self.menu_bar_label.pack()
        self.menu_bar_label.place(x=menu_pos[0], y=menu_pos[1], width=718, height=318)

        self.procceed_button_image = tk.PhotoImage(file="assets/buttons/procceed.png")
        self.procceed_button = tk.Button(master, image=self.procceed_button_image, command=self.procceed, bd=0, borderwidth=0)
        self.procceed_button.place(x=900, y = height / 1.15, width=100, height=48)

        for index, position in enumerate(vertexes_on_map):
            self.play_button = tk.Button(master, text = index, bd=0, borderwidth=0)
            self.play_button.place(x = position[0], y = position[1], width=20, height=20)

        

        self.menu_label_image = tk.PhotoImage(file="assets/buttons/menu_button.png")

        if not creature_on_vertex:
            self.menu_header_text = tk.Label(master, text = "Você se depara com um XXXX! O que fazer?", font = custom_font, bg="#CDA88E")
            self.menu_header_text.place(x=menu_pos[0] + 250, y=menu_pos[1] + 20, height= 50)

            for index, options in enumerate(fight_options):
                self.menu_label = tk.Label(master, text=options, image=self.menu_label_image, font = custom_font,compound=tk.CENTER, bd=0, borderwidth=0)
                self.menu_label.place(x=menu_pos[0] + 270, y=menu_pos[1] + 80 + 100*index, width=300, height=59)
        else: 
                self.menu_label = tk.Label(master, text="Procurar por recursos", font = custom_font, image=self.menu_label_image, compound=tk.CENTER, bd=0, borderwidth=0)
                self.menu_label.place(x=menu_pos[0] + 270, y=menu_pos[1] + 60, width=300, height=59)


    def procceed(self):
        global index, current_pos, path, current_vertex
        index += 1
        current_pos = path[index]
        current_vertex = graph.get(current_pos)
        print(current_vertex.getValue())

