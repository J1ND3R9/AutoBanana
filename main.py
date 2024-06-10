import os
import time as t
import pygetwindow as gw
import pyautogui as pag
import datetime
import keyboard
from colorama import init, Fore, Style

init()
clear = lambda: os.system("cls")


def openBanana(path):
    attempts = 6

    while attempts > 0:
        print(Fore.YELLOW + "Осталось попыток:", attempts)
        os.system(path)
        t.sleep(10)
        window = gw.getWindowsWithTitle("Banana")
        if window:
            clear()
            print(Fore.GREEN + "Успешно")
            return True
        print(Fore.RED + "Окно не найдено, повторяем...")
        attempts -= 1
    print(Fore.RED + "Ошибка запуска")
    quit()


def getWindowCoordinate():
    window = gw.getWindowsWithTitle("Banana")
    if window:
        win = window[0]
        center_x = win.left + win.width // 2
        center_y = win.top + win.height // 2
        return center_x, center_y
    else:
        return False


def clickOnBanana(time):
    if not getWindowCoordinate():
        quit()
    while time > 0:
        get_keyboard()
        x, y = getWindowCoordinate()
        pag.moveTo(x, y)
        pag.click()
        time -= 1
        t.sleep(1)


def get_keyboard():
    if keyboard.is_pressed("esc"):
        print(Fore.RED + "Остановка скрипта")
        quit()


path = input("Введите путь до Banana\n")
path.replace("\\", "/")
while 1:
    if "steamapps" not in path:
        path = input("Вы указали путь без Steam\n")
    elif "Banana.exe" not in path:
        path = input("Вы указали путь не к Banana\n")
    else:
        path.replace("\\", "/")
        path.replace('"', "")
        path.replace("'", "")
        clear()
        break

clickerQ = input("Включить кликер? (y/N)\n")
while clickerQ not in ("y", "N"):
    clear()
    clickerQ = input("Включить кликер? (y/N)\n")

clickerMode = True if clickerQ == "y" else False

print(Fore.RED + 'Закройте все окна, которые называются "Banana"!')
not_closed_window = gw.getWindowsWithTitle("Banana")
while 1:
    not_closed_window = gw.getWindowsWithTitle("Banana")
    if not not_closed_window:
        break
clear()


while 1:
    timerClick = 480
    timerWait = 10800
    print(Fore.YELLOW + "Запускаем Banana")
    openBanana(path)
    if clickerMode:
        clickOnBanana(timerClick)
    else:
        while timerClick > 0:
            get_keyboard()
            timerClick -= 1
            t.sleep(1)
    window = gw.getWindowsWithTitle("Banana")[0]
    window.close()
    now = datetime.datetime.now()
    print(Fore.YELLOW + "Закрытие в:", now.strftime("%H:%M"))
    while timerWait > 0:
        get_keyboard()
        timerWait -= 1
        t.sleep(1)
