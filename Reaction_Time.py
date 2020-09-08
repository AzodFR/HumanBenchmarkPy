#################################################################################################
#                                                                                               #
#   Author: Azod                                                                                #
#   Github: github.com/AzodFR                                                                   #
#   Comments: Just launch the script, strat the test and place the cursor on the red color       #
#                                                                                               #  
#################################################################################################
import pyautogui as pg

i = 0

while True:
    mouse = pg.position()
    if mouse.x == 0:
        break
    elif str(pg.pixel(mouse.x, mouse.y)) == "(75, 219, 106)":
        pg.click()
        print("Green !")
        i+=1
    if i == 5:
        break
        