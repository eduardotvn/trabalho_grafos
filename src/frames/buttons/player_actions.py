from game_funcs import check_for_items, check_point, move_creatures, check_creature_on_node, ress_explorator, ress_enemy, battle, check_treasure_vertex
from .global_variables import menu_pos, update_index, update_current_vertex, update_current_pos, get_path, get_index, get_current_pos, get_current_vertex, get_graph, get_player
import tkinter as tk
from tkinter import font

def procceed(self, action: str):
    from .show_menus import toggle_menu, show_found_treasure, show_checkpoint_saved
    index = get_index()
    if action == "procceed":
        update_index(index + 1)
    elif action == "flee":
        update_index(index - 1)
    update_current_pos()
    update_current_vertex()
    move_creatures(get_graph())
    self.creature_on_vertex = check_creature_on_node(get_current_pos())
    if self.creature_on_vertex is not None:
        self.clear_vertex = False
        toggle_menu(self, get_player(), self.treasure_font)
    else:
        self.clear_vertex = True
        toggle_menu(self, get_player(), self.treasure_font)
    if check_treasure_vertex(get_graph(), get_player(), get_current_pos()):
        show_found_treasure(self)
    check = check_point(get_graph(), get_player(), get_current_pos())
    if check:
        show_checkpoint_saved(self)
        

def fight(self):
    from .show_menus import toggle_menu, show_game_over
    results = battle(get_player(), self.creature_on_vertex)
    if(results.result == "MURDERER"):
        ress_enemy(self.creature_on_vertex, get_current_pos())
        self.vertex_clear()
        toggle_menu(self, get_player(), self.treasure_font)
    elif(results.result == "DIED"):
        if(get_player().getLives() > 0):
            ress_explorator(get_player())
            get_player().discountLife()
            self.vertex_clear()
            toggle_menu(self, get_player(), self.treasure_font)
            if get_player().hasCheckpoint():
                print("Renasci no checkpoint")
                new_pos = get_player().getVertexValue()
                update_index(new_pos)
                update_current_pos()
                self.ress_text = tk.Label(self.master, text = "Você morreu, restam " + str(get_player().getLives()) + " vidas", font=font.Font(family="Gabriola", size=24), bg="#CDA88E")
                self.ress_text.place(x=menu_pos[0] + 250, y=menu_pos[1] + 20, height=50)
                toggle_menu(self, get_player(), self.treasure_font)
            else:
                self.reset_pos_index()
                self.ress_text = tk.Label(self.master, text = "Você morreu, restam " + str(get_player().getLives()) + " vidas", font=font.Font(family="Gabriola", size=24), bg="#CDA88E")
                self.ress_text.place(x=menu_pos[0] + 250, y=menu_pos[1] + 20, height=50)
                toggle_menu(self, get_player(), self.treasure_font)
        else:
            show_game_over(self, 0)

def search_for_resources(self):
    from .show_menus import show_items
    items = check_for_items(get_graph(), get_current_pos())
    if len(items) == 0:
        print("Não há itens aqui")
    else:
        custom_font = font.Font(family="Gabriola", size=24)
        show_items(self, items, custom_font, get_current_vertex(), get_player())