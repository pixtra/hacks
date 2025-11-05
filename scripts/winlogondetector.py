import time
import pyautogui
while True:
    try:
        pixel_color = pyautogui.pixel(0, 0)
    except OSError:
        print("User is on ctrl + alt + del screen")
    else:
        print("User is not on ctrl + alt + del screen")
    time.sleep(1)
