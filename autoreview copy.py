import tkinter as tk
import pyautogui
import time
import random

def record_mouse_positions(clicks):
    positions = []

    for _ in range(clicks):
        # Get the current mouse position and add it to the list
        current_position = pyautogui.position()
        print(current_position)
        pos = tk.Label(text=current_position)
        pos.pack()
        positions.append(current_position)

        # Wait for 20 seconds
        time.sleep(5)

    return positions

def perform_mouse_actions(positions, num_repeats,base,upper,lower):
    
    for _ in range(num_repeats):
        wait_time = random.uniform(lower,upper)
        time.sleep(base + wait_time)

        time.sleep(1)
        # Move the mouse to the specified position
        pyautogui.moveTo(positions[0][0], positions[0][1])
        pyautogui.click(button='left')
        with pyautogui.hold('ctrl'):
            pyautogui.press('v')
        time.sleep(2)
        # Click the left 0mouse button
        pyautogui.moveTo(positions[1][0], positions[1][1])
        pyautogui.click(button='left')

            

if __name__ == "__main__":

    window = tk.Tk()
    delay = "wait 10 secs"
    
    clicks=2
    base = 10
    lower = 0
    upper = 10

    print("starting after 10 sec delay")
    time.sleep(10)
    
    # Run the function and print the recorded mouse positions
    recorded_positions = record_mouse_positions(clicks)
    print("Recorded Mouse Positions:")
    
    num_repeats = 140

    # Perform the mouse actions
    perform_mouse_actions(recorded_positions, num_repeats,base,lower,upper)

