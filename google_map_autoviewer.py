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

# Coordinates on Google maps in Bulgaria
BG_Sofia_map='https://www.google.cz/maps/@42.6977942,23.3210398,3a,75y,102.62h,71.07t/data=!3m6!1e1!3m4!1sEqiPw1QN92-8AVC5ky0HEg!2e0!7i13312!8i6656!6m1!1e1?hl=cs'
BG_Plovdiv_map='https://www.google.cz/maps/@42.1472198,24.7481798,3a,75y,344.19h,78.09t/data=!3m6!1e1!3m4!1sGfD9ssq_CynA43s0XLUZyQ!2e0!7i13312!8i6656!6m1!1e1?hl=cs'
BG_Stara_Zagora_map='https://www.google.cz/maps/@42.4240528,25.6255566,3a,75y,88.45h,79.35t/data=!3m6!1e1!3m4!1shvxQ66HS9HtwVTWSrR5g_Q!2e0!7i13312!8i6656!6m1!1e1?hl=cs'
BG_Burgas_map='https://www.google.cz/maps/@42.4936817,27.4723975,3a,75y,96.07h,75.63t/data=!3m6!1e1!3m4!1sA4bHAW3SsD5WL7R0BwGfTw!2e0!7i13312!8i6656?hl=cs'
BG_Varna_map='https://www.google.cz/maps/@43.2045882,27.9108968,3a,75y,342.42h,81.33t/data=!3m6!1e1!3m4!1smAUv2xQ8pOOlZ_f0Nh0jwQ!2e0!7i13312!8i6656!6m1!1e1?hl=cs'

# Choose your destination on Google maps
choice=0
while choice not in range(1,6):
      print('Cities in Bulgaria\n1. Sofia\n2. Plovdiv\n3. Stara Zagora\n4. Burgas\n5. Varna')
      print('ESC for quit')
      try:
      	  choice=int(raw_input('Your choice is: '))
      except ValueError:
          print "Not a number"

# Start point on Google maps
if choice==1:
   location_on_map=BG_Sofia_map
elif choice==2:
   location_on_map=BG_Plovdiv_map
elif choice==3:
   location_on_map=BG_Stara_Zagora_map
elif choice==4:
   location_on_map=BG_Burgas_map
elif choice==5:
   location_on_map=BG_Varna_map
else:
   print('Invalid choice. Exiting with error.')

subprocess.Popen([browser,location_on_map])

# Wait for 5 sec till the web page is fully loaded
time.sleep(7)

# How to start browser in maximized window?
# For Firefox press F11
full_screen_key=autopy.key.K_F11
autopy.key.tap(full_screen_key)

# Xmax,Ymax=pyautogui.size( )
Xmax,Ymax=autopy.screen.get_size()

# Making loop for several mouse clicks
while True:
 	# Move the mouse cursor to X,Y coordinates
 	# pyautogui.click(0.5*Xmax, 0.65*Ymax)
 	autopy.mouse.smooth_move(int(0.5*Xmax),int(0.65*Ymax))
 	autopy.mouse.click()
 	time.sleep(3)
