#################################################################################################
#                                                                                               #
#   Author: Azod                                                                                #
#   Github: github.com/AzodFR                                                                   #
#   Comments: Lauch the script, put cursor on the yellow "Start test" box then press Enter      #
#                                                                                               #
#################################################################################################

from pynput import keyboard
import pyautogui as pg

def on_press(key):
        if str(key) == "Key.enter":
            pg.click(clicks=2)
            return False
def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()