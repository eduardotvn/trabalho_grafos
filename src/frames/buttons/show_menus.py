import tkinter as tk

def show_clear_menu(self, master, custom_font):
    menu_pos = [360, 380]
    self.procceed_button_image = tk.PhotoImage(file="assets/buttons/procceed.png")
    self.procceed_button = tk.Button(master, image=self.procceed_button_image, command= lambda: self.procceed("procceed"), bd=0, borderwidth=0)
    self.procceed_button.place(x=900, y = 720 / 1.15, width=100, height=48)

    self.search_resources = tk.Button(master, text="Procurar por recursos", font = custom_font, command = self.search_for_resources,image=self.menu_label_image, compound=tk.CENTER, bd=0, borderwidth=0)
    self.search_resources.place(x=menu_pos[0] + 270, y=menu_pos[1] + 60, width=300, height=59)

def show_battle_menu(self, master, custom_font, enemy):
    menu_pos = [360, 380]
    self.menu_header_text = tk.Label(master, text= enemy.__class__.__name__+ "! O que fazer?", font=custom_font, bg="#CDA88E")
    self.menu_header_text.place(x=menu_pos[0] + 250, y=menu_pos[1] + 20, height=50)

    self.fight_button_image = tk.PhotoImage(file="assets/buttons/menu_button.png")
    self.fight_button = tk.Button(master, text="Lutar!", image=self.fight_button_image, command=self.fight ,font=custom_font, compound=tk.CENTER, bd=0, borderwidth=0)
    self.fight_button.place(x=menu_pos[0] + 270, y=menu_pos[1] + 80, width=300, height=59)

    self.flee_button_image = tk.PhotoImage(file="assets/buttons/menu_button.png")
    self.flee_button = tk.Button(master, text="Fugir", image=self.flee_button_image, command= lambda: self.procceed("flee") ,font=custom_font, compound=tk.CENTER, bd=0, borderwidth=0)
    self.flee_button.place(x=menu_pos[0] + 270, y=menu_pos[1] + 180, width=300, height=59)

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
    if hasattr(self, 'ress_text'):
        self.ress_text.destroy()

def toggle_menu(self):
    clear_menu(self)

    self.show_menu()
    self.clear_sprite_image()
    self.set_sprite_image()
    self.set_pos_on_frame()

def show_found_treasure(self):

    self.found_treasure_image = tk.PhotoImage(file="assets/buttons/found_treasure.png")
    self.found_treasure = tk.Button(self.master, image=self.found_treasure_image, command= lambda: clear_show_found_treasure(self), bd=0, borderwidth=0)
    self.found_treasure.place(x=1280/2, y=720/2, width=400, height=200)

def clear_show_found_treasure(self):
    if hasattr(self, 'found_treasure'):
        self.found_treasure.destroy()