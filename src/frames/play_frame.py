import tkinter as tk
from PIL import Image, ImageTk
from tkinter import PhotoImage
from src.models.search import *
from src.models.graph import *
from src.models.explorator import *
from src.game_funcs.battle import *
from src.game_funcs.creatures_movements import *
from src.game_funcs.get_sprites import *
from src.frames.buttons.show_menus import *
from tkinter import font


graph = readGraph('grafos/grafo1.txt')
player = Explorator(50, 5)

path = deepSearch(graph, graph.get(0))
index = 0
current_pos = path[index] 
current_vertex = graph.get(current_pos)
menu_pos = [360, 380]

move_creatures(graph)

class Play_Frame:
    def __init__(self, master, image_path, height, width):
        self.master = master
        self.master.title("Treasure Hunt")

        self.menu_label_image = tk.PhotoImage(file="assets/buttons/menu_button.png")
        image = Image.open(image_path)
        image = image.resize((width, height))
        photo = ImageTk.PhotoImage(image)
        self.creature_on_vertex = None 
        self.clear_vertex = True

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

        self.show_menu()
        self.set_sprite_image()

    def show_menu(self):
        custom_font = font.Font(family="Gabriola", size=24)
        if self.clear_vertex == True:
            show_clear_menu(self, self.master, custom_font)
        else:
            show_battle_menu(self, self.master, custom_font, self.creature_on_vertex)

    def procceed(self):
        global index, current_pos, path, current_vertex
        index += 1
        current_pos = path[index]
        current_vertex = graph.get(current_pos)
        move_creatures(graph)
        self.clear_sprite_image()
        self.set_sprite_image()
        self.creature_on_vertex = check_creature_on_node(current_pos)
        if self.creature_on_vertex is not None:
            self.clear_vertex = False
            self.toggle_menu()
        else:
            self.clear_vertex = True
            self.toggle_menu()

    def fight(self):
        results = battle(player, self.creature_on_vertex)
        if(results.result == "MURDERER"):
            print("Morreu")
            self.creature_on_vertex = None
            self.clear_vertex = True
            self.toggle_menu()
        elif(results.result == "DIED"):
            print("Voce morreu")

    def flee(self):
        global index, current_pos, path, current_vertex
        index -= 1
        current_pos = path[index]
        current_vertex = graph.get(current_pos)
        move_creatures(graph)
        self.clear_sprite_image()
        self.set_sprite_image()
        self.creature_on_vertex = check_creature_on_node(current_pos)
        if self.creature_on_vertex is not None:
            self.clear_vertex = False
            self.toggle_menu()
        else:
            self.clear_vertex = True
            self.toggle_menu()

    def search_for_resources(self):
        print("Searching")

    def toggle_menu(self):
        self.clear_menu()

        print("Clear Vertex : ", self.clear_vertex)
        self.show_menu()
        self.clear_sprite_image()
        self.set_sprite_image()
        
    def set_sprite_image(self):
        img_path = choose_image(self)
        self.sprite_photo = ImageTk.PhotoImage(file=img_path)        
        self.sprite_label = tk.Label(self.master, image=self.sprite_photo)
        self.sprite_label.place(x=menu_pos[0] + 38, y=menu_pos[1] + 62, width=194, height=198)
    
    def clear_sprite_image(self):
        self.sprite_label.destroy()

    def clear_menu(self):
        if hasattr(self, 'menu_header_text'):
            self.menu_header_text.destroy()
        if hasattr(self, 'fight_button'):
            self.fight_button.destroy()
        if hasattr(self, 'flee_button'):
            self.flee_button.destroy()
        if hasattr(self, 'search_resources'):
            self.search_resources.destroy()
        if hasattr(self, 'procceed_button'):
            self.procceed_button.destroy()