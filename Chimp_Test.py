#################################################################################################
#                                                                                               #
#   Author: Azod                                                                                #
#   Github: github.com/AzodFR                                                                   #
#   Comments: Lauch the script, put cursor on '1' then press A, do it in order then press       #
#             Enter ! To remove the laste cursor position, press Q                              #
#                                                                                               #
#################################################################################################

from pynput import keyboard
from pynput.mouse import Button, Controller
import pyautogui as pg

numbers = []
mouse = Controller()

def on_press(key):
    try:
        if key.char == 'a':
            numbers.append(mouse.position)
            print(numbers)
        elif key.char == 'q':
            if len(numbers)>0:
                numbers.pop()
    except AttributeError:
        print(key)
        if str(key) == "Key.enter":
            for pos in numbers:
                print(str(pos[0])+" / "+str(pos[1]))
                pg.click(x=pos[0], y=pos[1])
            numbers.clear()
def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()