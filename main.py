import tkinter as tk
from PIL import Image, ImageTk

class MainApp:
    def __init__(self, master, image_path, height, width):
        self.master = master
        self.master.title("Treasure Hunt")

        image = Image.open(image_path)
        image = image.resize((width, height))
        photo = ImageTk.PhotoImage(image)

        self.background_image = tk.Label(self.master, image=photo)
        self.background_image.photo = photo
        self.background_image.pack()

        self.play_button_image = tk.PhotoImage(file="assets/buttons/play_button.png")
        self.play_button = tk.Button(master, image=self.play_button_image, command=self.play_clicked)
        self.play_button.place(x=100, y=height / 6, width=400, height=150)

        self.options_button_image = tk.PhotoImage(file="assets/buttons/options_button.png")
        self.options_button = tk.Button(master, image=self.options_button_image, command=self.play_clicked)
        self.options_button.place(x=100, y=height / 2, width=400, height=150)

    def play_clicked(self):
        print("Play button clicked!")

if __name__ == "__main__":
    image_path = "assets/IlhaJPG.jpg"
    height = 720
    width = 1280

    root = tk.Tk()
    app = MainApp(root, image_path, height=height, width=width)
    root.mainloop()
