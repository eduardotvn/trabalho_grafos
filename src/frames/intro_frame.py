import tkinter as tk
from PIL import Image, ImageTk
from src.frames.play_frame import Play_Frame

class Intro_Frame:
    def __init__(self, master, image_path, height, width):
        self.master = master
        self.master.title("Treasure Hunt")

        image = Image.open(image_path)
        image = image.resize((width, height))
        photo = ImageTk.PhotoImage(image)

        self.background_image = tk.Label(self.master, image=photo)
        self.background_image.photo = photo
        self.background_image.pack()

        self.play_button_image = tk.PhotoImage(file="assets/buttons/start_button.png")
        self.play_button = tk.Button(master, image=self.play_button_image, command=self.start_playing, bd=0, borderwidth=0)
        self.play_button.place(x=1100, y = height / 1.15, width=100, height=48)

    def start_playing(self):
        self.background_image.pack_forget()
        self.play_button.place_forget()

        play_frame = Play_Frame(self.master, "assets/ilhaMapeada.jpg", 720, 1280)