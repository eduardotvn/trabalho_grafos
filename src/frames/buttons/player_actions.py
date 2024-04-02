from game_funcs import check_for_items, check_point, move_creatures, check_creature_on_node, ress_explorator, ress_enemy, battle, check_treasure_vertex, check_for_traps
from .global_variables import menu_pos, update_index, update_current_pos, get_index, get_current_pos, get_current_vertex, get_graph, get_player, get_checkpoint_index, get_path, get_move_count, update_move_count
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
    from .show_menus import toggle_menu, show_found_treasure, show_checkpoint_saved, show_victory, trap_button, show_game_over
    index = get_index()
    if index <= len(get_path()) - 1:
        if action == "procceed":
            update_index(index + 1)
        elif action == "flee":
            update_index(index - 1)
            get_player().getHitFrom(self.creature_on_vertex)
        update_current_pos()
        update_move_count()
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

        trap = check_for_traps(get_graph(), get_current_pos()) 
        if trap and trap.active():
            get_player().setDamage(trap.getDamage())
            trap_button(self, (trap.NAME + "! " + f"-{trap.DAMAGE} de vida."), self.trap_font)

        if check_point(get_graph(), get_current_pos(), get_index(), get_player()):
            show_checkpoint_saved(self)
            get_player().setCheckpoint(get_current_pos())
        
        if(get_index() == len(get_path()) - 1):
            show_victory(self, get_player(), self.victory_font)
        elif(get_move_count() == 3*get_graph().getN()):
            show_game_over(self, 1)
    
def fight(self):
    from .show_menus import show_game_over, toggle_menu

    results = battle(get_player(), self.creature_on_vertex)

    toggle_menu(self, get_player(), self.treasure_font)

    if(results.result == "MURDERER"):
        on_enemy_murdered(self)
    elif(results.result == "DIED" or get_player().getHp() <= 0):
        if(get_player().getLives() > 1):
            get_player().discountLife()
            if get_player().hasCheckpoint():
                ress_on_checkpoint(self)
            else:
                ress_on_beginning(self)
        else:
            show_game_over(self, 0)
    

def search_for_resources(self):
    from .show_menus import show_items
    items = check_for_items(get_graph(), get_current_pos())
    custom_font = font.Font(family="Gabriola", size=24)

    def weapons(x):
        from models import Weapon
        if issubclass(x.__class__, Weapon):
            return True
        else:
            return False
        
    def cures(x):
        from models import Cure
        if issubclass(x.__class__, Cure):
            return True
        else:
            return False

    filtered_arr = []
    if len(items) > 0:
        weapons_filter = filter(weapons, items)
        cures_filter = filter(cures, items)
        for weapon in weapons_filter:
            filtered_arr.append(weapon)
        for cure in cures_filter:
            filtered_arr.append(cure)

    show_items(self, filtered_arr, custom_font, get_current_vertex(), get_player())

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