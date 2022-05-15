from pywinauto import Application
from pywinauto.win32functions import (
    # GetCursorPos,
    Process_DPI_Awareness,
    SetProcessDpiAwareness,
    SetProcessDPIAware,
)
from win32api import GetCursorPos
from pywinauto.keyboard import KeyAction
from pywinauto.mouse import click, move
from pynput.mouse import Button, Controller
from get_window_position import get_window_position
from key_check import key_check
import re

from random import randint
from time import sleep


# SetProcessDpiAwareness(Process_DPI_Awareness["Process_System_DPI_Aware"])
SetProcessDPIAware()
mouse = Controller()

# find all the windows
app = Application(backend="win32")
app.connect(title="The House of the Dead Remake")
game_window = app.window(title="The House of the Dead Remake")
game_window.set_focus()


wrapper_object = game_window.wrapper_object().rectangle()
left = wrapper_object.left
top = wrapper_object.top
right = wrapper_object.right
bottom = wrapper_object.bottom
print(left, top, right, bottom)


def start():
    while True:
        print("waiting press B to start")
        if key_check() == "S":
            print("Starting")
            break
        sleep(0.3)


start()
sleep(2)
while True:

    if key_check() == "S":
        print("Ending")
        break
    x = randint(left + 150, right - 150)
    y = randint(top + 150, bottom - 150)
    move(coords=(x, y))
    print(f"Clicking to {x}, {y}")
    mouse.click(Button.left, 1)
