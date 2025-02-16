import pyautogui

def find_image_and_calculate_coordinates(image_to_find, base_image):
    # Take a screenshot of the screen
    screenshot = pyautogui.screenshot()

    # Find the location of the image within the screenshot
    location = pyautogui.locateOnScreen(image_to_find,confidence=0.7)

    if location is not None:
        # Calculate the coordinates based on the requirements
        found_x, found_y, found_width, found_height = location

        point_x = found_x + found_width // 2
        point_y = found_y + found_height // 2

        # Print the calculated coordinates
        print("Found image at coordinates:", (found_x, found_y))
        print("Calculated point coordinates:", (point_x, point_y))

        return point_x, point_y
    else:
        print("Image not found in the screenshot.")
        return None

# Provide the path to the image to find
image_to_find_path = "assets/resp_button.png"

# Define the region for the base image (optional, you can use the entire screen by omitting the region parameter)
base_image_region = (0, 0, 1920, 1080)  # Uncomment and adjust the coordinates and dimensions as needed

# Find image and calculate coordinates
coordinates = find_image_and_calculate_coordinates(image_to_find_path, base_image_region)

# Use the calculated coordinates as needed in your application
print(coordinates)