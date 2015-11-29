#!/bin/python

# Open Google maps on Varna, Bulgaria
# How to open the browser?
# Open street view
# How to set coordinates on Google maps?
# Position the mouse cursor at coordinates (0.5*Xmax, 0.75*Ymax

import pyautogui
import time
import subprocess
# import quartz

Xmax,Ymax=pyautogui.size( )
# Open a web browser
browser_linux='/usr/bin/google-chrome' #For Linux Fedora
browser_macosx='/Applications/Firefox.app/Contents/MacOS/firefox' #For MAC OS X 10.6 or above
browser_win32='C:\\Program Files\\Mozilla Firefox\\firefox.exe'
browser_win64='C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe'
location_on_map='https://www.google.cz/maps/@43.2266496,27.9258776,3a,75y,306.16h,74.88t/data=!3m6!1e1!3m4!1sJqD4dCizlZZln3Y0dh26-Q!2e0!7i13312!8i6656?hl=cs'

subprocess.Popen([browser_linux,location_on_map])

# Making loop for several mouse clicks
while True:
    # Move the mouse cursor to X,Y coordinates
    pyautogui.click(0.5*Xmax, 0.65*Ymax)
    time.sleep(3)
