import time
import mouse
import keyboard
import pyautogui
from time import sleep
from os import startfile
from pyautogui import locateCenterOnScreen, press, doubleClick, moveTo



# INIT---------------------------------------------------------------------------------------------------------------#



class Nome:


    def __init__(self):
        print("\nAbrindo epic games\n")
        pyautogui.PAUSE = 0.5
        self.loc_epicgames = "C:\Program Files (x86)\Epic Games\Launcher\Portal\Binaries\Win32\EpicGamesLauncher.exe"

    def Start(self):
        self.OpenEpicGames()
        self.OpenGame()

    def OpenEpicGames(self):
        startfile(self.loc_epicgames)

    def OpenGame(self):
        in_loop = True
        while in_loop:
            sleep(0.5)
            loc = locateCenterOnScreen(r'./data/GTA V.PNG', confidence=0.9)
            if loc is None:
                pass
            else:
                print('Abrindo game\n')
                moveTo(loc)
                doubleClick(loc)
                sleep(0.5)
                in_loop = False

    def LocButtonHistoryMode(self):
        in_loop = True
        while in_loop:
            sleep(0.5)
            button_1 = locateCenterOnScreen(r'./data/modohistoria2.PNG', confidence=0.9)
            if button_1 is None:
                pass
            else:
                for i in range(6):
                    press('enter')
                    sleep(0.5)
                in_loop = False

    def Carregando(self):
        in_loop = True
        while in_loop:
            sleep(0.5)
            carregando = locateCenterOnScreen(r'./data/carregando.png', confidence=0.9)
            carregando1 = locateCenterOnScreen(r'./data/carregando1.png', confidence=0.9)
            if carregando is None or carregando1 is None:
                pass
            else:
                print('O game foi aberto\n\nFinalizando altomacão, tenha uma boa jogatina!')
                in_loop = False


bot = Nome()
bot.Start()


# Finish-------------------------------------------------------------------------------------------------------------#

