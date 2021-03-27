# Rexulica
from PIL import ImageGrab , ImageOps
import pyautogui
import time
from time import sleep
from numpy import *
sleep(5)
#variabila cu care mutam cutia
muta= 3
#restart
buton_restart=(482,492)
#timp de inceput
inceput=time.time()
#cutie
box=(220,515,243,518)
#ajustare box
ajustare =70;
box = (box[0] + ajustare, box[1], box[2] + ajustare, box[3])
#
# pasare
pasare=(220+ajustare,483,243+ajustare,494)
pasare_jos=(220+ajustare,520,423+ajustare,530)
def restart():
    pyautogui.click(buton_restart)
def sari():
    pyautogui.keyDown('space')
    sleep(0.05)
    pyautogui.keyUp('sapce')
    print('am sarit')
    return 0
def jos():
    pyautogui.keyDown('down')
    sleep(0,15)
    pyautogui.keyUp('down')
def sarima_sau_sall():

    iamgine=ImageGrab.grab(box)
    gri=ImageOps.grayscale(iamgine)
    aux=array(gri.getcolors())
    aux= aux.sum()
    print(aux)
    if aux > 380:
        return 1
    return 0
def pasare_sau_sall():
    iamgine_pasare = ImageGrab.grab(pasare)
    imagine_pasare_jos = ImageGrab.grab(pasare_jos)
    gri_pasare_jos=ImageOps.grayscale(imagine_pasare_jos)
    gri_pasare = ImageOps.grayscale(iamgine_pasare)
    aux_pasare_jos=array(gri_pasare_jos.getcolors())
    aux_pasare = array(gri_pasare.getcolors())
    aux_pasare_jos = aux_pasare_jos.sum()
    aux_pasare = aux_pasare.sum()
    #print(aux_pasare_jos)
    if aux_pasare > 600 and aux_pasare_jos < 1000:
        print("am detectat pasrea")
        return 1
    return 0



restart()
while 1:
    if sarima_sau_sall():
        sari()



    if time.time() - inceput > 7:
         box = (box[0] + muta, box[1], box[2] + muta, box[3])
         inceput = time.time();
         print('am mutat')

    if pasare_sau_sall():
         print('stai jos')



