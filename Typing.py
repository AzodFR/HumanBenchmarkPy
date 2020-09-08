#################################################################################################
#                                                                                               #
#   Author: Azod                                                                                #
#   Github: github.com/AzodFR                                                                   #
#   Comments: Open the console and paste in the order the 2 codes to get the entire text       #
#                                                                                               #
#################################################################################################
#                                                                                               #
#   Code:                                                                                       #
""" 1: var script = document.createElement('script');
       script.src = "https://ajax.googleapis.com/ajax/libs/jquery/1.6.3/jquery.min.js";
       document.getElementsByTagName('head')[0].appendChild(script);
    2: $('.incomplete').text()"""
#                                                                                               #
#################################################################################################
from pynput import keyboard
import pyautogui as pg

pasted = 0
text = input("Paste the entire texte here: ")
print("Now click on the typing box and press Enter")
pasted = 1

def on_press(key):
    if pasted == 1:
        if str(key) == "Key.enter":
            pg.write(text)
            return False
def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()