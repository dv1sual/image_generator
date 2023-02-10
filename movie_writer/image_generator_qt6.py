import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QInputDialog, QMessageBox
from PyQt6.QtGui import QPixmap
from PIL import Image, ImageDraw
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


try:
    from PIL import Image, ImageDraw
except ImportError:
    QMessageBox.critical(None, "Error", "The Python Imaging Library (PIL) is not installed.")
    sys.exit()

app = QApplication(sys.argv)

width, ok = QInputDialog.getInt(None, "Image Generator", "Enter Width:", min=1)
if not ok:
    sys.exit()
height, ok = QInputDialog.getInt(None, "Image Generator", "Enter Height:", min=1)
if not ok:
    sys.exit()
num_images, ok = QInputDialog.getInt(None, "Image Generator", "Enter Number:", min=1)
if not ok:
    sys.exit()

color_options = [(255, 255, 255), (255, 255, 0), (0, 255, 255), (0, 255, 0), (255, 0, 255), (255, 0, 0), (0, 0, 255),
                 (0, 0, 0)]

directory = QFileDialog.getExistingDirectory(None, "Please select a folder to save the images")
if not directory:
    sys.exit()

for i in range(num_images):
    image = generate_test_pattern(width, height, color_options)
    image.save(f"{directory}/img_{i}.png")

sys.exit()
