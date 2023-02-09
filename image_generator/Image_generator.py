import tkinter as tk
from tkinter import simpledialog
from PIL import Image, ImageDraw
import random


def generate_test_pattern(img_width, img_height, colors):
    pattern = Image.new("RGB", (img_width, img_height), color=(0, 0, 0))
    draw = ImageDraw.Draw(pattern)
    bar_width = int(img_width / 8)
    for j in range(8):
        color = random.choice(colors)
        left = j * bar_width
        upper = 0
        right = (j + 1) * bar_width
        lower = img_height
        draw.rectangle((left, upper, right, lower), fill=color)
    return pattern


root = tk.Tk()
root.withdraw()

width = simpledialog.askinteger("Image Generator", "Enter the width of the image:", parent=root, minvalue=1)
height = simpledialog.askinteger("Image Generator", "Enter the height of the image:", parent=root, minvalue=1)
num_images = simpledialog.askinteger("Image Generator", "Enter the number of images to generate:", parent=root,
                                     minvalue=1)

color_options = [(255, 255, 255), (255, 255, 0), (0, 255, 255), (0, 255, 0), (255, 0, 255), (255, 0, 0), (0, 0, 255),
                 (0, 0, 0)]

for i in range(num_images):
    image = generate_test_pattern(width, height, color_options)
    image.save("img_{}.png".format(i))

root.destroy()
