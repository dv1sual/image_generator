# image_generator

# This script generates a series of simple test patterns, each with seven bars of random colors and a black border. The user can specify the dimensions and number of images to generate through dialogs.


This is a Python script using the Tkinter and PIL (Pillow) libraries to generate a series of test patterns as PNG images.

Here's what the code does, step by step:

The generate_test_pattern function generates a single test pattern. It takes three arguments: img_width, img_height, and colors. It creates a new image using the Image.new method and the "RGB" color mode. The image is filled with white.

The function then creates a drawing context using the ImageDraw.Draw class. It calculates the width of each bar in the pattern as img_width / 7 and generates seven bars with different colors.

The function draws a rectangle for each bar, with the color chosen from the colors argument. The function makes sure that each color is only used once by checking the previous_colors list.

The function draws four lines around the perimeter of the image, using the draw.line method, to create a border.

The function returns the pattern as an image.

The script creates a Tkinter Tk object and withdraws the main window, so that it doesn't display on the screen.

The script then uses the simpledialog.askinteger method to prompt the user for the width, height, and number of images to generate.

The script then calls the generate_test_pattern function repeatedly to generate the desired number of test patterns. Each pattern is saved to disk as a PNG file with a unique name, using the save method.

Finally, the script destroys the Tkinter Tk object to clean up.
