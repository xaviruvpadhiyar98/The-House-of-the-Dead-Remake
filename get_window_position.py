from win32gui import GetWindowText, EnumWindows, GetWindowRect, SetForegroundWindow
from win32com.client import Dispatch

windows_list = []


def enum_win(hwnd, result):
    win_text = GetWindowText(hwnd)
    windows_list.append((hwnd, win_text))


EnumWindows(enum_win, [])


def get_window_position(window_name):
    for (hwnd, win_text) in windows_list:
        if window_name.lower() in win_text.lower():
            game_hwnd = hwnd
            Dispatch("WScript.Shell").SendKeys("%")
            SetForegroundWindow(game_hwnd)
            return GetWindowRect(game_hwnd)


if __name__ == "__main__":
    position = get_window_position("_tb")
    print(position)
