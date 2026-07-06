import pyautogui
import time
import random
import sys
import time

x, y = 329, 795  # your chosen coordinates

print(f"Clicking at X:{x}, Y:{y} every 10ms. Press 'q' to stop.")

while True:
    if msvcrt.kbhit():
        key = msvcrt.getwch()
        if key.lower() == "q":
            print("\nStopped.")
            break
    pyautogui.click(x, y)
    time.sleep(0.0002)  # 10ms
