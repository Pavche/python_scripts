#!/bin/python

# Open Google maps on Varna, Bulgaria
# How to open the browser?
# Open street view
# How to set coordinates on Google maps?
# Position the mouse cursor at coordinates (0.5*Xmax, 0.75*Ymax

import pyautogui
import time
import subprocess

Xmax,Ymax=pyautogui.size( )
# Open a web browser
browser='/bin/google-chrome'
location_on_map='https://www.google.cz/maps/@43.2048071,27.9108268,3a,75y,357.62h,90.25t/data=!3m6!1e1!3m4!1sOCU_Az6N3o3XYteUv-VkMQ!2e0!7i13312!8i6656!6m1!1e1?hl=cs'

subprocess.Popen([browser,location_on_map])


# Making loop for several mouse clicks
while True:
    # Move the mouse cursor to X,Y coordinates
    pyautogui.click(0.5*Xmax, 0.65*Ymax)
    time.sleep(3)

