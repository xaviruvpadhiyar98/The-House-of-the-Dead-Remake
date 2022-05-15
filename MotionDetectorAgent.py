from pywinauto.win32functions import SetProcessDPIAware
from pywinauto.mouse import move
from pynput.mouse import Button, Controller
from key_check import key_check
from itertools import permutations
from typing import List, Tuple
from mss import mss
import cv2
import numpy as np
from grab_screen import grab_screen
from get_window_position import get_window_position
from time import sleep
from utils import (
    get_game_window,
    get_box_position,
    start,
)


def MotionDetectorAgent(position: List) -> None:
    i = 0

    while True:
        if key_check() == "S":
            print("Ending")
            break

        i += 1

        background = grab_screen(region=position)
        orig_image = background.copy()
        background = cv2.cvtColor(background, cv2.COLOR_BGR2GRAY)
        orig_image = cv2.resize(orig_image, (300, 300))
        cv2.imshow("Motion Detector", orig_image)
        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break

        if i % CONSECUTIVE_FRAME == 0 or i == 1:
            image_dff = []

        img = grab_screen(region=position)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        image_diff = cv2.absdiff(background, img)
        ret, thres = cv2.threshold(image_diff, 60, 255, cv2.THRESH_BINARY)

        image_dff.append(thres)
        if len(image_dff) == CONSECUTIVE_FRAME:
            sum_image = sum(image_dff)
            contours, _ = cv2.findContours(
                sum_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
            )
            # draw the contours on the original image
            for i, cnt in enumerate(contours):
                cv2.drawContours(img, contours, i, (0, 0, 255), 3)
            for contour in contours:
                # get the xmin, ymin, width, and height coordinates from the contours
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(orig_image, (x, y), (x + w, y + h), (255, 255, 255), 4)
                move(coords=(x + w // 2, y + h // 2))
                mouse.click(Button.left, 2)
                print(f"Clicking {x+w//2} {y+h//2}", end="\r")

        print(f"current frame: {i}", end="\r")
        sleep(0.01)


def main():
    start()
    sleep(2)
    position = get_window_position(window_name="The House of the Dead Remake")
    MotionDetectorAgent(position)


if __name__ == "__main__":
    # SET Default DPI
    SetProcessDPIAware()
    mouse = Controller()
    CONSECUTIVE_FRAME = 5
    main()
    cv2.destroyAllWindows()
