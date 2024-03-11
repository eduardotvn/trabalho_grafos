import os
import random

def choose_image(self):
    if self.creature_on_vertex is not None:
        creature_class = self.creature_on_vertex.__class__.__name__
        if creature_class == "Onca":
            return "assets/enemy_sprites/legendary_panther.png"
        elif creature_class == "FormigaQuimera":
            return "assets/enemy_sprites/chimaera_ant.png"
        else:
            return "assets/enemy_sprites/giant_crocodile.png"
    else: 
        all_files = os.listdir("assets/node_sprites")
        image_file = random.choice([f for f in all_files if os.path.isfile(os.path.join("assets/node_sprites", f))])
        full_path = os.path.join("assets/node_sprites", image_file)
        return full_path