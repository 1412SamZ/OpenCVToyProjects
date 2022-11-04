from tkinter import MOVETO
import pyautogui

import numpy as np

import pyautogui, sys
print('Press Ctrl-C to quit.')
i = 0
try:
    while i <= 20:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)

        num_seconds = 0.5
        pyautogui.moveRel(10, 10, duration=num_seconds)

        moveToX, moveToY = pyautogui.position() 
        num_of_clicks = 1
        secs_between_clicks = 0.5
        #pyautogui.click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=secs_between_clicks, button='right')
        i += 1
except KeyboardInterrupt:
    print('\n')


