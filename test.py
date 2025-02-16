import pyautogui
from pynput import mouse
from PIL import Image
import json

# Initialize global variables to store the coordinates
start_x, start_y = 0, 0
end_x, end_y = 0, 0

# Function to handle mouse click events
def on_click(x, y, button, pressed):
    global start_x, start_y, end_x, end_y
    if pressed:
        # On first click, record the start coordinates
        start_x, start_y = x, y
    else:
        # On release, record the end coordinates and stop listener
        end_x, end_y = x, y
        return False

def select_region():
    print("Please click and drag to select the region for the screenshot...")
    # Start the mouse listener to capture the region
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()

    # Return the selected region
    return (start_x, start_y, end_x, end_y)

def save_region_to_json(region, filename="region_coordinates.json"):
    coordinates = {
        "start_x": region[0],
        "start_y": region[1],
        "end_x": region[2],
        "end_y": region[3]
    }
    with open(filename, "w") as f:
        json.dump(coordinates, f)
    print(f"Region coordinates saved to {filename}")

def load_region_from_json(filename="region_coordinates.json"):
    with open(filename, "r") as f:
        coordinates = json.load(f)
    print(f"Region coordinates loaded from {filename}")
    return (coordinates["start_x"], coordinates["start_y"], coordinates["end_x"], coordinates["end_y"])

def capture_screenshot(region):
    # Calculate the width and height of the selected region
    x1, y1, x2, y2 = region
    width = x2 - x1
    height = y2 - y1

    # Capture the screenshot of the specified region
    screenshot = pyautogui.screenshot(region=(x1, y1, width, height))

    # Save the screenshot to a file
    screenshot.save("region_screenshot.png")

    # Optionally, open the screenshot
    screenshot.show()

if __name__ == "__main__":
    region = select_region()
    save_region_to_json(region)
    loaded_region = load_region_from_json()
    capture_screenshot(loaded_region)
