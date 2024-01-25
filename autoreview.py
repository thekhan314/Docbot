
import pyautogui
import time
import random

def record_mouse_positions(clicks):
    positions = []

    for _ in range(clicks):
        # Get the current mouse position and add it to the list
        current_position = pyautogui.position()
        print(current_position)
        positions.append(current_position)

        # Wait for 20 seconds
        time.sleep(5)

    return positions

def perform_mouse_actions(positions, num_repeats,base,upper,lower):
    
    for _ in range(num_repeats):
        wait_time = random.uniform(lower,upper)
        time.sleep(base + wait_time)
        pyautogui.moveTo(x=2090,y=660)
        pyautogui.click(button='left')
        pyautogui.press('pgdn')
        pyautogui.press('pgdn')
        pyautogui.press('pgdn')
        pyautogui.press('pgdn')
        for position in positions:
            time.sleep(1)
            # Move the mouse to the specified position
            pyautogui.moveTo(position[0], position[1])

            # Click the left 0mouse button
            pyautogui.click(button='left')

            

if __name__ == "__main__":
    
    clicks=5
    base = 10
    lower = 1
    upper = 4

    print("starting after 10 sec delay")

    time.sleep(7)
    # Run the function and print the recorded mouse positions
    recorded_positions = record_mouse_positions(clicks)
    print("Recorded Mouse Positions:")
    
    num_repeats = 184

    # Perform the mouse actions
    perform_mouse_actions(recorded_positions, num_repeats,base,lower,upper)

