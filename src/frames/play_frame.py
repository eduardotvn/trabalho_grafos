from game_funcs import check_for_items, scatter_cpoints, check_point, choose_image, move_creatures, check_creature_on_node, ress_explorator, ress_enemy, battle
from models import readGraph, Explorator
from searches import deepSearch, breadthFirstSearch
from .buttons import clear_menu, show_battle_menu, show_clear_menu, vertexes_on_map
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import font

graph = readGraph('grafos/grafo1.txt')
player = Explorator(50, 5)

path = deepSearch(graph, graph.get(0))
wide_path = breadthFirstSearch(graph, graph.get(0))
index = 0
current_pos = path[index] 
current_vertex = graph.get(current_pos)
menu_pos = [360, 380]

move_creatures(graph)
scatter_cpoints(graph)

class Play_Frame:
    def __init__(self, master, image_path, height, width):
        self.master = master
        self.master.title("Treasure Hunt")

        self.menu_label_image = tk.PhotoImage(file="assets/buttons/menu_button.png")
        image = Image.open(image_path)
        image = image.resize((width, height))
        photo = ImageTk.PhotoImage(image)
        self.vertex_clear()


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

        self.set_pos_on_frame()
        self.show_menu()
        self.set_sprite_image()

    def show_menu(self):
        custom_font = font.Font(family="Gabriola", size=24)
        if self.clear_vertex == True:
            show_clear_menu(self, self.master, custom_font)
        else:
            show_battle_menu(self, self.master, custom_font, self.creature_on_vertex)

    def procceed(self, action: str):
        global index, current_pos, path, current_vertex
        if action == "procceed":
            index += 1
        elif action == "flee":
            index -= 1
        current_pos = path[index]
        current_vertex = graph.get(current_pos)
        check_point(graph, player, current_pos)
        move_creatures(graph)
        self.creature_on_vertex = check_creature_on_node(current_pos)
        if self.creature_on_vertex is not None:
            self.clear_vertex = False
            self.toggle_menu()
        else:
            self.clear_vertex = True
            self.toggle_menu()
        print(current_pos)

    def fight(self):
        global lives, index, current_pos
        results = battle(player, self.creature_on_vertex)
        if(results.result == "MURDERER"):
            ress_enemy(self.creature_on_vertex, current_pos)
            self.vertex_clear()
            self.toggle_menu()
        elif(results.result == "DIED"):
            if(lives > 0):
                ress_explorator(player)
                lives -= 1
            self.vertex_clear()
            self.toggle_menu()
            self.reset_pos_index()
            self.ress_text = tk.Label(self.master, text = "Você morreu, restam " + str(lives) + " vidas", font=font.Font(family="Gabriola", size=24), bg="#CDA88E")
            self.ress_text.place(x=menu_pos[0] + 250, y=menu_pos[1] + 20, height=50)

    def search_for_resources(self):
        items = check_for_items(graph, current_pos)
        if len(items) == 0:
            print("Não há itens aqui")
        else:
            print(items)

    def toggle_menu(self):
        clear_menu(self)

        self.show_menu()
        self.clear_sprite_image()
        self.set_sprite_image()
        self.set_pos_on_frame()
        
    def set_sprite_image(self):
        img_path = choose_image(self)
        self.sprite_photo = ImageTk.PhotoImage(file=img_path)        
        self.sprite_label = tk.Label(self.master, image=self.sprite_photo)
        self.sprite_label.place(x=menu_pos[0] + 38, y=menu_pos[1] + 62, width=194, height=198)
    
    def clear_sprite_image(self):
        self.sprite_label.destroy()

    def vertex_clear(self):
        self.clear_vertex = True
        self.creature_on_vertex = None

    def reset_pos_index(self):
        global current_pos, index
        current_pos = 0
        index = 0

    def set_pos_on_frame(self):
        global current_pos
        if hasattr(self, 'player_pos'):
            self.player_pos.destroy()
        self.player_pos_img = tk.PhotoImage(file = "assets/buttons/player_pos.png")
        self.player_pos = tk.Label(self.master, image= self.player_pos_img, bd=0)
        self.player_pos.place(x = vertexes_on_map[current_pos][0], y = vertexes_on_map[current_pos][1], width=16, height=16)