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
    if hasattr(self, 'weapon_button'):
        self.weapon_button.destroy()
    if hasattr(self, 'treasure_icon'):
        self.treasure_icon.destroy()
    if hasattr(self, 'life_icon'):
        self.life_icon.destroy()
    if hasattr(self, 'game_over'):
        self.game_over.destroy()
    if hasattr(self, 'found_checkpoint'):
        self.found_checkpoint.destroy()
    if hasattr(self, 'no_weapon'):
        self.no_weapon.destroy()
    if hasattr(self, 'cure_button'):
        self.cure_button.destroy()
    if hasattr(self, 'alert_button'):
        self.alert_button.destroy()
    if hasattr(self,'hp_icon'):
        self.hp_icon.destroy()
    if hasattr(self, 'damage_icon'):
        self.damage_icon.destroy()