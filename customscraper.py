import pyautogui as pt

button = pt.locateOnScreen("resp_button.png")

# returns # returns (left, top, width, height) of matching region

buttonx, buttony = pt.center(button)
pt.click(buttonx,buttony)                                                                                                                                                                                                                                                                                                             