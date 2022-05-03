from pywinauto.win32functions import SetProcessDPIAware
from pywinauto.mouse import move
from pynput.mouse import Button, Controller
from key_check import key_check
from itertools import permutations
from typing import List, Tuple

from random import randint
from time import sleep
from utils import (
    get_game_window,
    get_box_position,
    start,
)


def RandomClickAgent(
    left: int,
    top: int,
    right: int,
    bottom: int,
    coordinates_to_click: List[Tuple[int, int]] = [],
) -> None:
    while True:
        if key_check() == "S":
            print("Ending")
            break

        for coord in coordinates_to_click:
            x, y = coord
            if left <= x <= right and top <= y <= bottom:
                print(f"Clicking to {x}, {y}", end="\r")
                move(coords=coord)
                mouse.click(Button.left, 5)
            # sleep(0.1)

    # SOMEWHAT RANDOM
    # start_x, start_y = 100, 100
    # end_x, end_y = right - 100, bottom - 100
    # for off_x in range(start_x, end_x, 100):
    #     for off_y in range(start_y, end_y, 100):
    #         print(f"Clicking to {off_x}, {off_y}", end="\r")
    #         move(coords=(off_x, off_y))
    #         mouse.click(Button.left, 1)
    #         sleep(0.1)

    ### FULL RANDOM
    # for off_x, off_y in range(start_x)
    # x = randint(left + offsetx, right - offsetx)
    # y = randint(top + offsety, bottom - offsety)
    # move(coords=(x, y))
    # print(f"Clicking to {x}, {y}", end="\r")
    # mouse.click(Button.left, 1)


def main():
    game_window = get_game_window(title="The House of the Dead Remake")
    left, top, right, bottom = get_box_position(game_window)
    print(f"left {left}, top {top}, right {right}, bottom {bottom}")
    coordinates_to_click = list(permutations(range(left + 80, right - 80, 110), 2))
    # print(f"Total coordinates to click: {len(coordinates_to_click)}")
    # print(f"Coordinate values - {coordinates_to_click}")
    start()
    sleep(2)
    RandomClickAgent(
        left, top, right, bottom, coordinates_to_click=coordinates_to_click
    )


if __name__ == "__main__":
    # SET Default DPI
    SetProcessDPIAware()
    mouse = Controller()
    main()
