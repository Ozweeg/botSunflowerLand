import pyautogui as pag
import random
from pathes import *
import time



pag.FAILSAFE = False

def random_move(cordlist):
    destx=cordlist[0]
    desty=cordlist[1]
    x, y = pag.position() # Current Position
    moves = random.randint(2,3)
    pixelsx = destx-x
    pixelsy = desty-y
    avgpixelsx = pixelsx/moves
    avgpixelsy = pixelsy/moves
    #print ("Pixels to be moved X: ", pixelsx," Y: ",pixelsy, "Number of mouse movements: ", moves, "Avg Move X: ", avgpixelsx, " Y: ", avgpixelsy)

    while moves > 0:
            offsetx = (avgpixelsx+random.randint(-2, random.randint(1,5)))
            offsety = (avgpixelsy+random.randint(-2, random.randint(1,4)))
            #print (x + offsetx, y + offsety, moves)
            pag.moveTo(x + offsetx, y + offsety, duration=0.0024)
            moves = moves-1
            if moves > 0:
                avgpixelsx = pixelsx / moves
                avgpixelsy = pixelsy / moves

def moveClick(file_name):
    cordlist=GetCord(file_name)
    random_move(cordlist)
    pag.click()

def GetCord(file_path):
    centre=pag.locateCenterOnScreen(file_path, confidence=0.8)
    if centre == None:
        return None
    return (list(centre))

def open_inv():
    moveClick(inv_pic)
    print("Inventory opened")
    return 0

def close_inv():
    moveClick(inv_close)
    print("Inventory closed")
    return 0

def choose_seed(seed_pathes):
    open_inv()
    time.sleep(0.6)
    for seed in seed_pathes:
        if GetCord(seed) != None:
            print(seed, " found in inventory")
            moveClick(seed)
            break
        else:
            print(seed, " not found in inventory")
    time.sleep(1)
    close_inv()
    return 0

def plant_seeds():
    i = 0
    while GetCord(hole_pic) != None:
        moveClick(hole_pic)
        i += 1
        if i == 5:
            check_seeds()
            i = 0

def grab_plants():
    for plant in plants_pathes:
        i = 0
        while GetCord(plant) != None:
            moveClick(plant)
            i += 1
            if i == 10:
                check_troubles()
                i = 0

def check_troubles():
        if GetCord(chest_pic) != None:
            chest_cord=GetCord(chest_pic)
            print("Chest found at:", GetCord(chest_pic))
            pag.click(chest_cord,duration=1)
            moveClick(close_text)
        elif GetCord(find_txt) != None:
            print("Goblin detected!")
            moveClick(find_txt)
            time.sleep(1)
            pag.press('f12')
            time.sleep(1)
            pag.hotkey('ctrl', 'f')
            pag.write('goblin_jump')
            time.sleep(0.66)
            for i in range(0, 999):
                print("try ", i)
                if GetCord(stealer) != None:
                    moveClick(stealer)
                    break
            time.sleep(0.8)
            pag.press('f12')
            time.sleep(0.7)
            moveClick(continue_txt)

def check_seeds():
    for ns in no_seed_pathes:
        if GetCord(ns) != None:
            print("No seeds!")
            choose_seed(seed_pathes)

def check_disconnect():
    if GetCord(disconnect_pic) != None:
        moveClick(continue_txt)
        time.sleep(5)
        moveClick(refresh_pic)
        time.sleep(5)
        moveClick(lets_farm_txt)
        time.sleep(7)


    print("No troubles left")
    return 0

x_start=420
while True:
    pag.click(x_start,1060)
    check_troubles()
    check_disconnect()
    choose_seed(seed_pathes)
    grab_plants()
    plant_seeds()
    x_start+=48
    if x_start > 708:
        x_start=420

