import tkinter as tk
from PIL import Image, ImageTk
from .intro_frame import Intro_Frame

image_path = "assets/mapaIlha.jpg"

class Main_Frame:
    def __init__(self, master, height, width):
        self.master = master
        self.master.title("Treasure Hunt")

        image = Image.open(image_path)
        image = image.resize((width, height))
        photo = ImageTk.PhotoImage(image)

        self.background_image = tk.Label(self.master, image=photo)
        self.background_image.photo = photo
        self.background_image.pack()

        self.play_button_image = tk.PhotoImage(file="assets/buttons/play_button.png")
        self.play_button = tk.Button(master, image=self.play_button_image, command=self.start_playing, bd=0, borderwidth=0)
        self.play_button.place(x=100, y = height / 1.55, width=200, height=65)


    def start_playing(self):
        self.background_image.pack_forget()
        self.play_button.place_forget()

        Intro_Frame(self.master, "assets/procuradoNickelBottoms.jpg", 720, 1280)