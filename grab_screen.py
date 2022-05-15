import numpy as np
from win32gui import GetDesktopWindow, GetWindowDC, ReleaseDC, DeleteObject
from win32ui import CreateDCFromHandle, CreateBitmap
from win32con import SRCCOPY


def grab_screen(region):

    hwin = GetDesktopWindow()

    left, top, x2, y2 = region
    width = x2 - left + 1
    height = y2 - top + 1

    hwindc = GetWindowDC(hwin)
    srcdc = CreateDCFromHandle(hwindc)
    memdc = srcdc.CreateCompatibleDC()
    bmp = CreateBitmap()
    bmp.CreateCompatibleBitmap(srcdc, width, height)
    memdc.SelectObject(bmp)
    memdc.BitBlt((0, 0), (width, height), srcdc, (left, top), SRCCOPY)

    signedIntsArray = bmp.GetBitmapBits(True)
    img = np.fromstring(signedIntsArray, dtype="uint8")
    img.shape = (height, width, 4)

    srcdc.DeleteDC()
    memdc.DeleteDC()
    ReleaseDC(hwin, hwindc)
    DeleteObject(bmp.GetHandle())

    return img


if __name__ == "__main__":
    import cv2

    image = grab_screen((100, 100, 400, 400))

    cv2.imshow("test_img", image)
    cv2.waitKey()
