import tkinter as tk
from .player_actions import fight, procceed
from .clear_frames import clear_menu

def show_battle_menu(self, master, custom_font, enemy):
    menu_pos = [360, 380]
    self.menu_header_text = tk.Label(master, text= enemy.__class__.__name__+ "! O que fazer?", font=custom_font, bg="#CDA88E")
    self.menu_header_text.place(x=menu_pos[0] + 250, y=menu_pos[1] + 20, height=50)

    self.fight_button_image = tk.PhotoImage(file="assets/buttons/menu_button.png")
    self.fight_button = tk.Button(master, text="Lutar!", image=self.fight_button_image, command= lambda: fight(self) ,font=custom_font, compound=tk.CENTER, bd=0, borderwidth=0)
    self.fight_button.place(x=menu_pos[0] + 270, y=menu_pos[1] + 80, width=300, height=59)

    self.flee_button_image = tk.PhotoImage(file="assets/buttons/menu_button.png")
    self.flee_button = tk.Button(master, text="Fugir", image=self.flee_button_image, command= lambda: procceed(self, "flee") ,font=custom_font, compound=tk.CENTER, bd=0, borderwidth=0)
    self.flee_button.place(x=menu_pos[0] + 270, y=menu_pos[1] + 180, width=300, height=59)

def show_items(self, items: list, custom_font, vertex, explorator):
    from models import Weapon
    menu_pos = [360, 380]

    self.weapon_background_image = tk.PhotoImage(file="assets/buttons/menu_button.png")
    self.no_weapon_image = tk.PhotoImage(file="assets/buttons/menu_button.png")
    if len(items) > 0:
        print(items)
        for i, item in enumerate(items):
            if issubclass(item.__class__, Weapon):
                self.weapon_button = tk.Button(self.master, text=item.__class__.__name__, image=self.weapon_background_image, command= lambda item=item: get_weapon(self, explorator, item, vertex, custom_font), font=custom_font, compound=tk.CENTER, bd=0, borderwidth=0)
                self.weapon_button.place(x=menu_pos[0] + 270, y=menu_pos[1] + 80 + 100*i, width=300, height=59)
            else: 
                self.cure_button = tk.Button(self.master, text=item.__class__.__name__, image=self.weapon_background_image, command= lambda item=item: get_cure(self, explorator, item, vertex, custom_font), font=custom_font, compound=tk.CENTER, bd=0, borderwidth=0)
                self.cure_button.place(x=menu_pos[0] + 270, y=menu_pos[1] + 80 + 100*i, width=300, height=59)

        self.procceed_button_image = tk.PhotoImage(file="assets/buttons/procceed.png")
        self.procceed_button = tk.Button(self.master, image=self.procceed_button_image, command= lambda: procceed(self, "procceed"), bd=0, borderwidth=0)
        self.procceed_button.place(x=900, y = 720 / 1.15, width=100, height=48)
    else:
        self.no_weapon = tk.Button(self.master, text="Não há itens aqui...", image=self.no_weapon_image, command = lambda: print(), font=custom_font, compound=tk.CENTER, bd=0, borderwidth=0)
        self.no_weapon.place(x=menu_pos[0] + 270, y=menu_pos[1] + 80, width=300, height=59)

        self.procceed_button_image = tk.PhotoImage(file="assets/buttons/procceed.png")
        self.procceed_button = tk.Button(self.master, image=self.procceed_button_image, command= lambda: procceed(self, "procceed"), bd=0, borderwidth=0)
        self.procceed_button.place(x=900, y = 720 / 1.15, width=100, height=48)

def toggle_menu(self, explorator, custom_font):
    clear_menu(self)

    show_current_treasure(self, explorator, custom_font)
    show_current_life(self, explorator, custom_font)
    show_current_hp(self, explorator, custom_font)
    show_current_damage(self, explorator, custom_font)
    self.show_menu()
    self.clear_sprite_image()
    self.set_sprite_image()
    self.set_pos_on_frame()

def show_found_treasure(self):

    self.found_treasure_image = tk.PhotoImage(file="assets/buttons/found_treasure.png")
    self.found_treasure = tk.Button(self.master, image=self.found_treasure_image, command= lambda: clear_show_found_treasure(self), bd=0, borderwidth=0)
    self.found_treasure.place(x=1280/2, y=720/2, width=400, height=200)
    
    self.procceed_button_image = tk.PhotoImage(file="assets/buttons/procceed.png")
    self.procceed_button = tk.Button(self.master, image=self.procceed_button_image, command= lambda: procceed(self, "procceed"), bd=0, borderwidth=0)
    self.procceed_button.place(x=900, y = 720 / 1.15, width=100, height=48)

def clear_show_found_treasure(self):
    if hasattr(self, 'found_treasure'):
        self.found_treasure.destroy()
    if hasattr(self, 'procceed_button'):
        self.procceed_button.destroy()


def get_weapon(self, explorator, weapon, vertex, custom_font):
    old_weapon = explorator.setWeapon(weapon)
    vertex.removeItem(weapon)
    if old_weapon:
        vertex.addItem(old_weapon)
    toggle_menu(self, explorator, custom_font)

def get_cure(self, explorator, cure, vertex, custom_font):

    if explorator.getHp() == explorator.getMaxHp():
         alert_button(self, "Sua vida está cheia", custom_font)
    else:
        explorator.setHeal(cure.use())
        vertex.removeItem(cure)
        toggle_menu(self, explorator, custom_font)

def show_current_treasure(self, explorator, custom_font):

    self.treasure_image = tk.PhotoImage(file= "assets/buttons/treasure_icon.png")
    self.treasure_icon = tk.Label(self.master, text=explorator.getTreasurePocket(), image=self.treasure_image, compound=tk.CENTER, font=custom_font, height=55, width=55)
    self.treasure_icon.place(x = 30, y = 30)
    

def show_current_life(self, explorator, custom_font):

    self.life_image = tk.PhotoImage(file= "assets/buttons/life_icon.png")
    self.life_icon = tk.Label(self.master, text = explorator.getLives(), image=self.life_image, compound=tk.CENTER, font=custom_font, height=55, width=55)
    self.life_icon.place(x= 30, y = 100)
    

def show_current_hp(self, explorator, custom_font):
    self.hp_image = tk.PhotoImage(file = "assets/buttons/hp_icon.png")
    self.hp_icon = tk.Label(self.master, text = explorator.getHp(), image=self.hp_image, compound=tk.CENTER, font=custom_font, height=55, width=55)
    self.hp_icon.place(x= 30, y = 170)
    

def show_current_damage(self, explorator, custom_font):
    self.damage_image = tk.PhotoImage(file = "assets/buttons/damage_icon.png")
    self.damage_icon = tk.Label(self.master, text = explorator.getAttack(), image=self.damage_image, compound=tk.CENTER, font=custom_font, height=55, width=55)
    self.damage_icon.place(x= 30, y = 240)
    

def show_checkpoint_saved(self):

    self.found_checkpoint_image = tk.PhotoImage(file= "assets/buttons/found_checkpoint.png")
    self.found_checkpoint = tk.Button(self.master, image=self.found_checkpoint_image, command= lambda: clear_show_found_checkpoint(self), bd=0, borderwidth=0)
    self.found_checkpoint.place(x=1280/2, y=720/2, width=400, height=200)

def clear_show_found_checkpoint(self):
    if hasattr(self, 'found_checkpoint'):
        self.found_checkpoint.destroy()

def show_game_over(self, type):

    self.game_over_death_image = tk.PhotoImage(file= "assets/buttons/game_over_death.png")
    self.game_over_time_image = tk.PhotoImage(file= "assets/buttons/game_over_time.png")

    if type == 0:
        self.game_over = tk.Button(self.master, image=self.game_over_death_image, command=self.reset_game, bd=0, borderwidth=0)
        self.game_over.place(x=1280/2, y=720/2, width=400, height=200)
    else:
        self.game_over = tk.Button(self.master, image=self.game_over_time_image, bd=0, borderwidth=0)
        self.game_over.place(x=1280/2, y=720/2, width=400, height=200)

def alert_button(self, message, custom_font):
    self.alert_image = tk.PhotoImage(file="assets/buttons/menu_button.png")
    self.alert_button = tk.Button(self.master,text = message, image = self.alert_image, command=lambda: self.alert_button.destroy(), compound=tk.CENTER, font=custom_font)
    self.alert_button.place(x=1280/2, y=720/2, width=299, height=59)
