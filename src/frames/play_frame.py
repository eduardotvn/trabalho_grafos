from game_funcs import scatter_cpoints, move_creatures, set_treasure_vertex, scatter_item, scatter_traps_func
from .buttons import show_battle_menu, vertexes_on_map, toggle_menu, menu_pos, update_index, update_current_pos, update_current_vertex, reset_player, reset_graph, reset_path, get_current_pos, get_graph, get_player, search_for_resources, show_icons, set_sprite_image
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import font

move_creatures(get_graph())
scatter_cpoints(get_graph())
set_treasure_vertex(get_graph())
scatter_item(get_graph())
scatter_traps_func(get_graph())

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

        self.custom_font = font.Font(family="Gabriola", size=24)
        self.treasure_font = font.Font(family="Gabriola", size=48)
        self.victory_font = font.Font(family="Gabriola", size=18, weight='bold')
        self.trap_font = font.Font(family='Grabiola', size=16)
        show_icons(self, get_player(), self.treasure_font)
        self.set_pos_on_frame()
        self.show_menu()
        set_sprite_image(self)

    def show_menu(self):
        if self.clear_vertex == True:
            search_for_resources(self)
        else:
            show_battle_menu(self, self.master, self.custom_font, self.creature_on_vertex)

    def vertex_clear(self):
        self.clear_vertex = True
        self.creature_on_vertex = None

    def set_pos_on_frame(self):
        current_pos = get_current_pos()
        if hasattr(self, 'player_pos'):
            self.player_pos.destroy()
        self.player_pos_img = tk.PhotoImage(file = "assets/buttons/player_pos.png")
        self.player_pos = tk.Label(self.master, image= self.player_pos_img, bd=0)
        self.player_pos.place(x = vertexes_on_map[current_pos][0], y = vertexes_on_map[current_pos][1], width=16, height=16)

    def reset_game(self):
        reset_player(1)
        reset_graph()
        reset_path()
        update_index(0)
        update_current_pos() 
        update_current_vertex()

        move_creatures(get_graph())
        scatter_cpoints(get_graph())
        set_treasure_vertex(get_graph())
        scatter_item(get_graph())

        self.vertex_clear()

        toggle_menu(self, get_player(), self.treasure_font)

