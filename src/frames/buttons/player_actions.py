from game_funcs import check_for_items, check_point, move_creatures, check_creature_on_node, ress_explorator, ress_enemy, battle, check_treasure_vertex
from .global_variables import menu_pos, update_index, update_current_vertex, update_current_pos, get_path, get_index, get_current_pos, get_current_vertex, get_graph, get_player, get_checkpoint_index
import tkinter as tk
from tkinter import font

def procceed(self, action: str):
    """
    Irá lidar com seguir pelo grafo ou fugir.\n
    Recebendo ''proceed'' como parâmetro irá seguir,\n
    enquanto ''flee'' resultará em fuga. A função se \n
    encarrega de atualizar as posições e checar \n
    possíveis criaturas e checkpoints.
    """
    from .show_menus import toggle_menu, show_found_treasure, show_checkpoint_saved
    index = get_index()
    if action == "procceed":
        update_index(index + 1)
    elif action == "flee":
        update_index(index - 1)

    update_current_pos()
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

    if check_point(get_graph(), get_current_pos(), get_index(), get_player()):
        show_checkpoint_saved(self)
        get_player().setCheckpoint(get_current_pos())
        
def fight(self):
    from .show_menus import toggle_menu, show_game_over

    results = battle(get_player(), self.creature_on_vertex)


    if(results.result == "MURDERER"):
        on_enemy_murdered(self)
    elif(results.result == "DIED"):
        if(get_player().getLives() > 1):
            get_player().discountLife()
            if get_player().hasCheckpoint():
                ress_on_checkpoint(self)
            else:
                ress_on_beginning(self)
        else:
            show_game_over(self, 0)
    elif(results.result == "BOTH_DIED"):
        both_died(self)
    

def search_for_resources(self):
    from .show_menus import show_items
    items = check_for_items(get_graph(), get_current_pos())
    if len(items) == 0:
        print("Não há itens aqui")
    else:
        custom_font = font.Font(family="Gabriola", size=24)
        show_items(self, items, custom_font, get_current_vertex(), get_player())

def both_died(self):
    from .show_menus import toggle_menu, show_game_over
    if(get_player().getLives() > 1):
        on_enemy_murdered()
        get_player().discountLife()
        if get_player().hasCheckpoint():
            ress_on_checkpoint(self)
        else:
            ress_on_beginning(self)
    else:
        show_game_over(self, 0)

def on_enemy_murdered(self):
    from .show_menus import toggle_menu
    ress_enemy(self.creature_on_vertex, get_current_pos())
    self.vertex_clear()
    toggle_menu(self, get_player(), self.treasure_font)

def ress_on_checkpoint(self):
    from .show_menus import toggle_menu
    self.vertex_clear()
    ress_explorator(get_player())
    new_pos = get_checkpoint_index()
    update_index(new_pos)
    update_current_pos()
    toggle_menu(self, get_player(), self.treasure_font)
    self.ress_text = tk.Label(self.master, text = "Você morreu, restam " + str(get_player().getLives()) + " vidas", font=font.Font(family="Gabriola", size=24), bg="#CDA88E")
    self.ress_text.place(x=menu_pos[0] + 250, y=menu_pos[1] + 20, height=50)
    self.set_pos_on_frame()

def ress_on_beginning(self):
    from .show_menus import toggle_menu
    self.vertex_clear()
    ress_explorator(get_player())
    update_index(0)
    update_current_pos()
    toggle_menu(self, get_player(), self.treasure_font)
    self.ress_text = tk.Label(self.master, text = "Você morreu, restam " + str(get_player().getLives()) + " vidas", font=font.Font(family="Gabriola", size=24), bg="#CDA88E")
    self.ress_text.place(x=menu_pos[0] + 250, y=menu_pos[1] + 20, height=50)
    self.set_pos_on_frame()