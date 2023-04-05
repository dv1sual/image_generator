import pyautogui
from PIL import Image
import cv2
import numpy as np
from screeninfo import get_monitors
import time


# Capture the screenshot of a specific monitor
def capture_screenshot_of_monitor(monitor):
    screenshot = pyautogui.screenshot(region=(monitor.x, monitor.y, monitor.width, monitor.height))
    screenshot_np = np.array(screenshot)
    return screenshot_np


# Get the list of available monitors
def get_monitor_list():
    return get_monitors()


def print_info(message):
    red = "\033[91m"
    reset = "\033[0m"
    print(f"{red}[INFO] - {message}", flush=True)


def convert_color_space(image_np, color_space):
    if color_space == "YCrCb":
        converted_image = cv2.cvtColor(image_np, cv2.COLOR_RGB2YCrCb)
    else:
        converted_image = image_np
    return converted_image


def test_pixel_values(image, roi, color_space, expected_values, tolerance=0):
    x, y, w, h = roi
    region = image[y:y + h, x:x + w]

    if isinstance(expected_values, tuple):
        if color_space == "YCrCb":
            region = cv2.cvtColor(region, cv2.COLOR_RGB2YCrCb)
            expected_values = np.array(expected_values)
        elif color_space == "RGB":
            expected_values = np.array(expected_values)
        else:
            raise ValueError("Unsupported color space. Use 'RGB' or 'YCrCb'.")

        if expected_values.shape != (3,):
            raise ValueError("Expected values must be a tuple of three integers.")

        lower_bound = expected_values - tolerance
        upper_bound = expected_values + tolerance

        lower_bound = lower_bound.reshape(1, 1, -1)
        upper_bound = upper_bound.reshape(1, 1, -1)

        mask = cv2.inRange(region, lower_bound, upper_bound)
        if not np.all(mask == 255):
            actual_value = region[0, 0]
            print_info(f"Actual pixel value: {actual_value}")

        return np.all(mask == 255)
    else:
        raise ValueError("Expected values must be a tuple.")


# Show the captured image
def show_screenshot(screenshot_np):
    # Convert the image from RGB to BGR format for OpenCV
    bgr_screenshot = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)

    # Display the screenshot
    cv2.imshow('Screenshot', bgr_screenshot)
    print_info("Press 'q' to close the window and continue...")

    while True:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()


def main():
    # Get the list of available monitors
    print_info("Getting the list of available monitors...")
    monitors = get_monitor_list()
    time.sleep(2)
    print_info(f"Found {len(monitors)} monitor(s)")
    time.sleep(2)

    # Select the desired monitor (e.g., the second monitor)
    monitor_to_capture = monitors[0]
    print_info(f"Selected monitor {monitor_to_capture}")
    time.sleep(2)

    # Capture the screen of the selected monitor
    print_info("Capturing the screen of the selected monitor...")
    screenshot_np = capture_screenshot_of_monitor(monitor_to_capture)
    time.sleep(2)

    # Set the color space for comparison (no conversion needed)
    color_space = "RGB"
    print_info(f"Using the {color_space} color space for comparison")
    time.sleep(2)

    # Test the pixel values
    print_info("Testing the pixel values...")
    roi = (840, 525, 1680, 1050)  # Define the region of interest (ROI)
    time.sleep(2)
    print_info(f"Testing pixel values in the ROI: {roi}")
    time.sleep(2)
    # Show the captured image
    print_info("Showing the captured image...")
    x, y, w, h = roi
    region = screenshot_np[y:y + h, x:x + w]
    text = str(region[0, 0])
    cv2.putText(screenshot_np, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    show_screenshot(screenshot_np)
    time.sleep(2)
    expected_values = (0, 255, 0)  # Define the expected RGB values
    tolerance = 5  # Define the tolerance (optional)
    result = test_pixel_values(screenshot_np, roi, color_space, expected_values, tolerance)
    time.sleep(2)

    if result:
        print_info("Test passed: The pixel values meet the expected criteria.")
    else:
        print_info("Test failed: The pixel values do not meet the expected criteria.")


if __name__ == "__main__":
    main()
