#!/bin/python

# Open Google maps on Varna, Bulgaria
# How to open the browser?
# Open street view
# How to set coordinates on Google maps?
# Position the mouse cursor at coordinates (0.5*Xmax, 0.75*Ymax

# GUI automatization, works under Linux, paritially working unider Win64, not working under MAC OS X 10.8
import pyautogui
#GUI automatization works under Windows, Linux
import autopy
import time
import platform # Info about computer platform uder which the script is run
import os
import subprocess
# import quartz #For GUI under OS X on iMAC

# List of web browsers under various OS
# '/usr/bin/firefox' #For Linux Fedora
# '/Applications/Firefox.app/Contents/MacOS/firefox' #For MAC OS X 10.6 or above
# 'C:\\Program Files\\Mozilla Firefox\\firefox.exe' #For Windows 32-bit
# 'C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe' #For Windows 64-bit


# What OS are we running?
os_platform=platform.system()
os_replease=platform.release()
os_ver=platform.version()

# What is the default browser? Open with it Google maps.
browser=os.getenv('BROWSER')
location_on_map='https://www.google.cz/maps/@43.2266496,27.9258776,3a,75y,306.16h,74.88t/data=!3m6!1e1!3m4!1sJqD4dCizlZZln3Y0dh26-Q!2e0!7i13312!8i6656?hl=cs'
subprocess.Popen([browser,location_on_map])
# How to start browser in maximized window?

# Xmax,Ymax=pyautogui.size( )
Xmax,Ymax=autopy.screen.get_size()

# Making loop for several mouse clicks
while True:
	# Move the mouse cursor to X,Y coordinates
	# pyautogui.click(0.5*Xmax, 0.65*Ymax)
	autopy.mouse.smooth_move(int(0.5*Xmax),int(0.65*Ymax))
	autopy.mouse.click()
	time.sleep(3)
