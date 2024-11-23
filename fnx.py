#prefire pip install pyautogui pynput

import pyautogui
from pynput.mouse import Listener
import time

def execute_macro():
    pyautogui.click() #shoot

    pyautogui.press('z') #wall

    # Second click
    pyautogui.click() #place wall

    # Press 'Q'
    pyautogui.press('q') # get out of building mode

# Function to detect the mouse click event
def on_click(x, y, button, pressed):
    if button.name == 'button8' and pressed:
        print("Mouse Button 4 detected, executing macro.")
        execute_macro()

# Start listening for mouse events
with Listener(on_click=on_click) as listener:
    print("Press Mouse Button 4 (back button) to execute the macro.")
    listener.join()
