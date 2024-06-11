import os
from os import system
import time as t
import pygetwindow as gw
import pyautogui as pag
import datetime
import keyboard
import sys
from colorama import init, Fore, Style

init()
system("AutoBanana")
clear = lambda: os.system("cls")


def openBanana(path):
    attempts = 6

    while attempts > 0:
        print(Fore.YELLOW + "Attempts remaining:", attempts)
        os.system(path)
        t.sleep(10)
        window = gw.getWindowsWithTitle("Banana")
        if window:
            clear()
            print(Fore.GREEN + "Successfully found the window")
            return True
        print(Fore.RED + "Window is not found, repeat...")
        attempts -= 1
    print(Fore.RED + "Launching error")
    input("Close program")
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


def banana_window_is_exist():
    window = gw.getWindowsWithTitle("Banana")
    if window:
        return True
    return False


def get_keyboard():
    if keyboard.is_pressed("esc"):
        print(Fore.RED + "Stop script")
        quit()


if not os.path.exists("config.txt"):
    path = input("Insert path to Banana.exe\n")
    path.replace("\\", "/")
    while 1:
        if "steamapps" not in path:
            path = input("No steamapps in file path\n")
        elif "Banana.exe" not in path:
            path = input("No Banana.exe in file path\n")
        elif not os.path.isfile(path):
            path = input("File is not exist\n")
        else:
            path = path.replace("\\", "/")
            path = path.replace('"', "")
            path = path.replace("'", "")
            clear()
            break

    clickerQ = input("Enable autoclicker? (y/N)\n")
    while clickerQ not in ("y", "N"):
        clear()
        clickerQ = input("Enable autoclicker? (y/N)\n")

    clickerMode = True if clickerQ == "y" else False
else:
    config = open("config.txt", "r")
    try:
        path = config.readline().strip()
        path = path.replace("\\", "/")
        path = path.replace('"', "")
        path = path.replace("'", "")
        print(path)
        if "steamapps" not in path:
            raise ValueError("No steamapps in file path")
        elif "Banana.exe" not in path:
            raise ValueError("No Banana.exe in file path")
        elif not os.path.exists(path):
            raise ValueError("File is not exist")
    except ValueError as ve:
        print(Fore.RED + f"ERROR: {ve}")
        input("Close program")
        quit()
    try:
        clickerQ = config.readline().strip()
        clickerMode = True if clickerQ == "y" else False
        if clickerQ not in ("y", "N"):
            raise ValueError("Cannot read clicker mode (excepted: 'y' or 'N')")
    except ValueError as ve:
        print(Fore.RED + f"ERROR: {ve}")
        input("Close program")
        quit()

print(
    Fore.RED
    + 'Close all windows with title "Banana"!\nOr skip the warn by pressing the HOME key'
)
not_closed_window = gw.getWindowsWithTitle("Banana")
while 1:
    not_closed_window = gw.getWindowsWithTitle("Banana")
    if keyboard.is_pressed("esc"):
        quit()
    if not not_closed_window or keyboard.is_pressed("home"):
        break
clear()


while 1:
    timerClick = 480
    timerWait = 10800
    print(Fore.YELLOW + "Launching Banana")
    openBanana(path)
    if clickerMode:
        clickOnBanana(timerClick)
    else:
        while timerClick > 0:
            get_keyboard()
            if not banana_window_is_exist():
                print(Fore.RED + "\n\nProcess is interrupted")
                input("Close program")
                quit()
            sys.stdout.write("\r")
            sys.stdout.write(f"{timerClick} seconds remaining")
            sys.stdout.flush()
            timerClick -= 1
            t.sleep(1)
    window = gw.getWindowsWithTitle("Banana")[0]
    window.close()
    now = datetime.datetime.now()
    clear()
    print(Fore.YELLOW + "Closing time:", now.strftime("%H:%M"))
    while timerWait > 0:
        get_keyboard()
        sys.stdout.write("\r")
        sys.stdout.write(f"{timerWait} seconds remaining")
        sys.stdout.flush()
        timerWait -= 1
        t.sleep(1)
