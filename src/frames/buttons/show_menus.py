import tkinter as tk

def show_clear_menu(self, master, custom_font):
    menu_pos = [360, 380]
    self.procceed_button_image = tk.PhotoImage(file="assets/buttons/procceed.png")
    self.procceed_button = tk.Button(master, image=self.procceed_button_image, command=self.procceed, bd=0, borderwidth=0)
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
    self.flee_button = tk.Button(master, text="Fugir", image=self.flee_button_image, command=self.search_for_resources ,font=custom_font, compound=tk.CENTER, bd=0, borderwidth=0)
    self.flee_button.place(x=menu_pos[0] + 270, y=menu_pos[1] + 180, width=300, height=59)