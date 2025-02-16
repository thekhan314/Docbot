
import pyautogui
import time
import random
import tkinter as tk
from tkinter import messagebox
import time


def record_mouse_positions(clicks):
    positions = []
    box_txt = ''''''
    for _ in range(clicks):
        # Get the current mouse position and add it to the list
        current_position = pyautogui.position()

        print(current_position)
        
        box_txt += "\n Click [ {} ], {}".format(str(_),str(current_position))
        
        messagebox.showinfo("DOCBOT", box_txt)

        positions.append(current_position)

        # Wait for 20 seconds
        time.sleep(5)

    return positions

def perform_mouse_actions(positions, num_repeats,base,upper,lower):
    
    for _ in range(num_repeats):
        
        wait_time = random.uniform(lower,upper)
        wait_time = base + wait_time
        msg = "DOCBOT", "ITERATION : {} , \n wait_time: {} ".format(str(_),str(wait_time))
        print(msg)
        #messagebox.showinfo("Iterator", msg)
        #messagebox.withdraw
        time.sleep(wait_time)
        #messagebox.withdraw
        # Move the mouse to the specified position
        for position in positions:
            time.sleep(1)
            # Move the mouse to the specified position
            pyautogui.moveTo(position[0], position[1])

            # Click the left 0mouse button
            pyautogui.click(button='left')
    print(time.time())

        

            

if __name__ == "__main__":

    pyautogui.FAILSAFE = False

    # Create the main application window+

    num_repeats = 100
    clicks=3
    base = 60
    lower = 30
    upper = 60

    print("starting after 10 sec delay")

    time.sleep(10)
    # Run the function and print the recorded mouse positions
    recorded_positions = record_mouse_positions(clicks)
    print("Recorded Mouse Positions:")
    
    

    # Perform the mouse actions
    perform_mouse_actions(recorded_positions, num_repeats,base,lower,upper)

                                                                              