try:
    import tkinter as tk
    from tkinter import simpledialog
    from PIL import Image, ImageDraw
except ModuleNotFoundError:
    print("Error: Required libraries (tkinter, PIL) are not installed.")
    exit(1)

import random


def generate_test_pattern(img_width, img_height, colors):
    pattern = Image.new("RGB", (img_width, img_height), color=(255, 255, 255))
    draw = ImageDraw.Draw(pattern)
    bar_width = int(img_width / 7)
    previous_colors = []
    for j in range(7):
        color = random.choice(colors)
        while color in previous_colors:
            color = random.choice(colors)
        previous_colors.append(color)
        left = j * bar_width
        upper = 0
        right = (j + 1) * bar_width
        lower = img_height
        draw.rectangle((left, upper, right, lower), fill=color)
    draw.line((0, 0, img_width, 0), fill=(0, 0, 0), width=4)
    draw.line((0, 0, 0, img_height), fill=(0, 0, 0), width=4)
    draw.line((0, img_height, img_width, img_height), fill=(0, 0, 0), width=4)
    draw.line((img_width, 0, img_width, img_height), fill=(0, 0, 0), width=4)
    return pattern


root = tk.Tk()
root.withdraw()

width = simpledialog.askinteger("Image Generator", "Enter Width:", parent=root, minvalue=1)
height = simpledialog.askinteger("Image Generator", "Enter Height:", parent=root, minvalue=1)
num_images = simpledialog.askinteger("Image Generator", "Enter Number:", parent=root,
                                     minvalue=1)

color_options = [(255, 255, 255), (255, 255, 0), (0, 255, 255), (0, 255, 0), (255, 0, 255), (255, 0, 0), (0, 0, 255),
                 (0, 0, 0)]

for i in range(num_images):
    image = generate_test_pattern(width, height, color_options)
    image.save("img_{}.png".format(i))

root.destroy()
