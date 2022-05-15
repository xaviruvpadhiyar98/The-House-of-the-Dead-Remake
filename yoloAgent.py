from pywinauto.win32functions import SetProcessDPIAware
from pywinauto.mouse import move, click
from pynput.mouse import Button, Controller
from key_check import key_check
from typing import List, Tuple
import cv2
from grab_screen import grab_screen
from common_functions import (
    get_game_window,
    get_box_position,
    start,
)
from time import sleep
from pathlib import Path
import torch


# model = torch.hub.load("ultralytics/yolov5", "yolov5s", verbose=False)
model = torch.hub.load(
    "ultralytics/yolov5", "custom", r"yolo_models\best_third_gen.pt", verbose=False
)
results_dir = Path("results")
runs_dir = Path("runs")
results_dir.mkdir(exist_ok=True)


def YoloAgent(position: List) -> None:
    start()
    sleep(1)
    i = 0

    while True:
        # i += 1
        # ZOMBIE_COUNT = 0
        # HUMAN_COUNT = 0
        if key_check() == "S":
            print("Ending")
            break

        image = grab_screen(region=position)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        results = model(image)
        results_info = results.pandas().xyxy[0].to_dict(orient="records")

        cv2.imshow("Testing", results.render()[0])
        if (cv2.waitKey(1) & 0xFF) == ord("q"):
            cv2.destroyAllWindows()
            break

        for results in results_info[::-1]:
            if results["name"] != "human":
                x = (int(results["xmin"]) + int(results["xmax"])) // 2
                y = (int(results["ymin"]) + int(results["ymax"])) // 2
                move(coords=(x, y))
                mouse.click(Button.left, 1)
                print(
                    f"found total {len(results_info)} - {results['name']} at {x}, {y}"
                )
                # cv2.imwrite(f"{results_dir}/{i}.png", image)


if __name__ == "__main__":
    SetProcessDPIAware()
    mouse = Controller()
    game_window = get_game_window("The House of the Dead Remake")
    position = get_box_position(game_window)
    print(position)
    YoloAgent(position)
