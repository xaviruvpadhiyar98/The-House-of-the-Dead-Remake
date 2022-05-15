from typing import Tuple
from pywinauto import Application
from pywinauto import WindowSpecification
from random import randint
from key_check import key_check
from time import sleep
import math

# "The House of the Dead Remake"
def get_game_window(title: str) -> WindowSpecification:
    app = Application()
    app.connect(title=title)
    game_window = app.window(title=title)
    game_window.set_focus()
    return game_window


def get_box_position(game_window: WindowSpecification) -> Tuple[int, int, int, int]:
    wrapper_object = game_window.wrapper_object().rectangle()
    return (
        wrapper_object.left,
        wrapper_object.top,
        wrapper_object.right,
        wrapper_object.bottom,
    )


def start() -> None:
    while True:
        print(f"waiting press S to start{'.'*randint(0,3)}", end="\r")
        if key_check() == "S":
            print("Starting")
            break
        sleep(0.3)


def spiral(radius, step, resolution=0.1, angle=0.0, start=0.0):
    dist = start + 0.0
    coords = []
    while dist * math.hypot(math.cos(angle), math.sin(angle)) < radius:
        cord = []
        cord.append(dist * math.cos(angle))
        cord.append(dist * math.sin(angle))
        coords.append(cord)
        dist += step
        angle += resolution
    return coords


# FIND ALL PERMUATIONS VALUES FOR THE GAME
from itertools import permutations

list(permutations(range(1, 10), 2))
