# This script shows largest cities in Bulgaria on Google maps
# using "street view" mode
# For some cities there are several starting points when looking at the map

# Script for Windows

# GUI automatization works under Windows, Linux
import pyautogui
import time
import platform # Info about computer platform uder which the script is run
import os
import subprocess
import sys
import random
import webbrowser

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
# Varinat 1 - from environment variables from the OS
#if os_platform=='Windows':
#   browser='C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe'
#elif os_platform=='Linux':
#   browser=os.getenv('BROWSER')
#else:
#   browser='UNKNOWN'


# Coordinates on Google maps in Bulgaria
BG_Sofia_map='https://www.google.cz/maps/@42.6977942,23.3210398,3a,75y,102.62h,71.07t/data=!3m6!1e1!3m4!1sEqiPw1QN92-8AVC5ky0HEg!2e0!7i13312!8i6656!6m1!1e1?hl=cs'
BG_Plovdiv_map='https://www.google.cz/maps/@42.1472198,24.7481798,3a,75y,344.19h,78.09t/data=!3m6!1e1!3m4!1sGfD9ssq_CynA43s0XLUZyQ!2e0!7i13312!8i6656!6m1!1e1?hl=cs'
BG_Stara_Zagora_map='https://www.google.cz/maps/@42.4240528,25.6255566,3a,75y,88.45h,79.35t/data=!3m6!1e1!3m4!1shvxQ66HS9HtwVTWSrR5g_Q!2e0!7i13312!8i6656!6m1!1e1?hl=cs'
BG_Burgas_map='https://www.google.cz/maps/@42.4936817,27.4723975,3a,75y,96.07h,75.63t/data=!3m6!1e1!3m4!1sA4bHAW3SsD5WL7R0BwGfTw!2e0!7i13312!8i6656?hl=cs'
BG_Varna_map={
'cathedral':'https://www.google.cz/maps/@43.2046937,27.9108173,3a,75y,343.6h,80.57t/data=!3m6!1e1!3m4!1svtMhmXJ-b_ITuagCoK03zw!2e0!7i13312!8i6656?hl=cs',
'center':'https://www.google.com/maps/@43.2033645,27.9129974,3a,75y,316.87h,87.15t/data=!3m6!1e1!3m4!1sNL_E4gOsVylzgb20UixEdA!2e0!7i13312!8i6656',
'railway_station':'https://www.google.com/maps/@43.1986025,27.9119716,3a,75y,147.52h,85.69t/data=!3m6!1e1!3m4!1slY1pM-SURUu_cfHg2MU2pA!2e0!7i13312!8i6656!6m1!1e1',
'central_post':'https://www.google.com/maps/@43.206677,27.910787,3a,75y,245.92h,88.56t/data=!3m6!1e1!3m4!1sYLkH3-V6bJB1IlYU1CwHbA!2e0!7i13312!8i6656',
'harbor':'https://www.google.com/maps/@43.1947194,27.9215336,3a,75y,189.58h,82.41t/data=!3m6!1e1!3m4!1szT0ajbfXUVR8KAVD4mzv-A!2e0!7i13312!8i6656',
'festival_congress_center':'https://www.google.com/maps/@43.2041814,27.9215867,3a,90y,69.92h,89.87t/data=!3m6!1e1!3m4!1sHiRr3RGiWFDL6R5uBU1ANg!2e0!7i13312!8i6656'
} # 6 locations in Varna

# Choose your destination on Google maps
choice=0
while choice not in range(1,6):
      print('Cities in Bulgaria\n1. Sofia\n2. Plovdiv\n3. Stara Zagora\n4. Burgas\n5. Varna')
      print('Q for quit')
      choice=raw_input('Your choice is: ')
      if choice=='q' or choice=='Q':
         sys.exit(0) 
      try:
         choice=int(choice) # Try to read as a number
      except:
         print('Not a number')

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
   #Chosing a start point from 6 locations in a random manner
   start_point={1:'cathedral',2:'center',3:'railway_station',4:'central_post',5:'harbor',6:'festival_congress_center'}
   pad = start_point[random.randint(1,6)]
   location_on_map=BG_Varna_map[pad]
else:
   print('Invalid choice. Exiting with error.')
   sys.exit(1)

# Variant 1 open the web browser
# subprocess.Popen([browser,location_on_map])
# Variant 2 open the web browser
webbrowser.open_new(location_on_map)

# Wait for 10 sec till the web page is fully loaded
time.sleep(10)

# How to start browser in maximized window?
# For browsers linke Firefox, Chrome, Midori under Linux press F11
# For browsers linke Firefox, Chrome under Windows press F11
if os_platform=='Linux' or os_platform=='Windows':
   pyautogui.press('f11')

Xmax,Ymax=pyautogui.size( )
# Xmax,Ymax=autopy.screen.get_size()
# This function works on a single display only, when using multiple monitors
# the script does not function properly


# Making loop for several mouse clicks
while True:
 	# Move the mouse cursor to X,Y coordinates then click
 	# Variant 1 - using automatization with AutoPy
        # autopy.mouse.smooth_move(int(0.5*Xmax),int(0.65*Ymax))
 	# autopy.mouse.click()
        # Variant 2 - using automatization with PyAutoGUI
	pyautogui.moveTo(0.5*Xmax, 0.65*Ymax,duration=1)
	pyautogui.click()
	time.sleep(3)
 	
# Written by Pavlin Georgiev
# November 2015
# Last update: 6 Dec 2015
