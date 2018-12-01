#!/usr/bin/env python
# This script shows largest cities in Bulgaria on Google maps
# using "street view" mode
# For some cities there are several starting points when looking at the map
# Python 3 is required for this script.

# How to install automation module PyAutoGUI?
# See: http://pyautogui.readthedocs.io/en/latest/install.html


# GUI automation works under Windows, Linux, and macOS
import pyautogui
from time import sleep
import platform # Info about computer platform uder which the script is run
import os
import subprocess
import sys
import random
import webbrowser


# What OS are we running?
os_platform = platform.system()
os_replease = platform.release()
os_ver = platform.version()


# Coordinates on Google maps in Bulgaria
BG_Sofia_map = 'https://www.google.cz/maps/@42.6977942,23.3210398,3a,75y,102.62h,90t/data=!3m6!1e1!3m4!1sEqiPw1QN92-8AVC5ky0HEg!2e0!7i13312!8i6656!6m1!1e1'
BG_Plovdiv_map = 'https://www.google.cz/maps/@42.1472198,24.7481798,3a,75y,344.19h,90t/data=!3m6!1e1!3m4!1sGfD9ssq_CynA43s0XLUZyQ!2e0!7i13312!8i6656!6m1!1e1'
BG_Stara_Zagora_map = 'https://www.google.cz/maps/@42.4240528,25.6255566,3a,75y,88.45h,90t/data=!3m6!1e1!3m4!1shvxQ66HS9HtwVTWSrR5g_Q!2e0!7i13312!8i6656!6m1!1e1'
BG_Burgas_map = 'https://www.google.cz/maps/@42.4936817,27.4723975,3a,75y,96.07h,90t/data=!3m6!1e1!3m4!1sA4bHAW3SsD5WL7R0BwGfTw!2e0!7i13312!8i6656'
BG_Varna_map = {
    'cathedral': 'https://www.google.cz/maps/@43.2046937,27.9108173,3a,75y,343.6h,90t/data=!3m6!1e1!3m4!1svtMhmXJ-b_ITuagCoK03zw!2e0!7i13312!8i6656',
    'center': 'https://www.google.com/maps/@43.2033645,27.9129974,3a,75y,316.87h,90t/data=!3m6!1e1!3m4!1sNL_E4gOsVylzgb20UixEdA!2e0!7i13312!8i6656',
    'railway station': 'https://www.google.com/maps/@43.1986025,27.9119716,3a,75y,147.52h,90t/data=!3m6!1e1!3m4!1slY1pM-SURUu_cfHg2MU2pA!2e0!7i13312!8i6656!6m1!1e1',
    'central post': 'https://www.google.com/maps/@43.2053704,27.9107392,3a,75y,354.51h,90t/data=!3m6!1e1!3m4!1s34K84rcVn36eLhLRk7Sv3A!2e0!7i13312!8i6656',
    'harbor': 'https://www.google.com/maps/@43.1947194,27.9215336,3a,75y,189.58h,90t/data=!3m6!1e1!3m4!1szT0ajbfXUVR8KAVD4mzv-A!2e0!7i13312!8i6656',
    'festival congress center': 'https://www.google.com/maps/@43.2052132,27.9201237,3a,75y,135.13h,90t/data=!3m6!1e1!3m4!1scpINnl3NXN38bYsJbUnIdw!2e0!7i13312!8i6656',
    'baba_Dzanka': 'https://www.google.com/maps/@43.2102584,27.9104829,3a,75y,260.36h,90t/data=!3m6!1e1!3m4!1s6JfqH0FS1xtkYaKeFXg-6w!2e0!7i13312!8i6656!6m1!1e1',
    'Central bus station': 'https://www.google.com/maps/@43.2158997,27.8956269,3a,75y,118.49h,90t/data=!3m6!1e1!3m4!1s8SuC_QOCCIey2VdhoO1YaA!2e0!7i13312!8i6656',
    'North entry point': 'https://www.google.com/maps/@43.2231588,27.8686577,3a,75y,106.75h,90t/data=!3m6!1e1!3m4!1sAFJsRd2vh5KMDo555E3mXg!2e0!7i13312!8i6656',
    'South-east entry point': 'https://www.google.com/maps/@43.185381,27.8749907,3a,75y,70.14h,90t/data=!3m6!1e1!3m4!1s65iz3MLdPVbRXlc4qxvmJA!2e0!7i13312!8i6656',
    '3rd March bul': 'https://www.google.com/maps/@43.2427395,27.8490392,3a,75y,95.38h,90t/data=!3m6!1e1!3m4!1sZEeucMlEWsRcRzMMfJ76rw!2e0!7i13312!8i6656',
    'Slivnica bul': 'https://www.google.com/maps/@43.2291763,27.8687948,3a,75y,107.48h,90t/data=!3m6!1e1!3m4!1sxSvNfzMz_jWfU3d6Rphk9g!2e0!7i13312!8i6656',
    'Maritime garden beach': 'https://www.google.com/maps/@43.1982567,27.9203401,3a,75y,46.51h,90t/data=!3m6!1e1!3m4!1sqbhknweypHuCLrjfiNFgxQ!2e0!7i13312!8i6656',
    'Maritime garden pantheon': 'https://www.google.com/maps/@43.2059094,27.9263633,3a,75y,60.99h,90t/data=!3m6!1e1!3m4!1sV3_wx3z1JqA8A8xX0nh96w!2e0!7i13312!8i6656',
    'Maritime garden zoo': 'https://www.google.com/maps/@43.2098006,27.9356122,3a,75y,73.29h,90t/data=!3m6!1e1!3m4!1st1vrD8Rrz-d1QAw0CcOrtA!2e0!7i13312!8i6656',
    'Maritime garden ajacent trees': 'https://www.google.com/maps/@43.2121187,27.9364853,3a,75y,148.57h,90t/data=!3m6!1e1!3m4!1syEsZ9PzfPMQR6rw6Divf5g!2e0!7i13312!8i6656',
    'Dolphinarium': 'https://www.google.com/maps/@43.2132686,27.9457041,3a,75y,252.61h,90t/data=!3m6!1e1!3m4!1sZMbs0JsPt4sLpemJrLN5Gw!2e0!7i13312!8i6656',
    'Chaika 4B': 'https://www.google.com/maps/@43.2152885,27.9504401,3a,75y,316.5h,90t/data=!3m6!1e1!3m4!1sXet_axqpgWyYrwHCzgMy3A!2e0!7i13312!8i6656',
    'Chaika 1': 'https://www.google.com/maps/@43.2245434,27.9414039,3a,75y,219.66h,90t/data=!3m6!1e1!3m4!1sIS1WP6sfonXnPuBshz1zMg!2e0!7i13312!8i6656',
    'Sport palace': 'https://www.google.com/maps/@43.2124797,27.9365382,3a,75y,240h,90t/data=!3m6!1e1!3m4!1sCAzLx8pKXrr436W1dDVesg!2e0!7i13312!8i6656',
    'Varna.net': 'https://www.google.cz/maps/place/Varna+Net/@43.2004684,27.9130576,3a,75y,78h,90t/data=!3m7!1e1!3m5!1sLaszH5bl39lgxqYQmJqc6Q!2e0!6s%2F%2Fgeo3.ggpht.com%2Fcbk%3Fpanoid%3DLaszH5bl39lgxqYQmJqc6Q%26output%3Dthumbnail%26cb_client%3Dsearch.TACTILE.gps%26thumb%3D2%26w%3D86%26h%3D86%26yaw%3D78.71454%26pitch%3D0%26thumbfov%3D100!7i13312!8i6656!4m5!3m4!1s0x40a453f4104aa431:0x4fae7ee6806b0300!8m2!3d43.2004488!4d27.913232!6m1!1e1',

}  # Various interesting locations in Varna on the map

Pavkamemories = {
    'Nikola': 'https://www.google.bg/maps/@43.2137679,27.9072112,3a,75y,224.85h,90t/data=!3m6!1e1!3m4!1s7rz4PX-ZC8dtw4-HOdEXgQ!2e0!7i13312!8i6656',
    'baba na Vesko': 'https://www.google.bg/maps/@43.2237154,27.9205595,3a,75y,270.36h,90t/data=!3m6!1e1!3m4!1sEX-2K7FgonImhHd4LFddMA!2e0!7i13312!8i6656',
    'elementary school': 'https://www.google.com/maps/@43.2098919,27.9093612,3a,75y,342.82h,90t/data=!3m6!1e1!3m4!1s5WIKDYCpOx7zmT_UMjk5Ag!2e0!7i13312!8i6656',
    'secondary school': 'https://www.google.bg/maps/@43.2166186,27.9522045,3a,75y,335.76h,90t/data=!3m6!1e1!3m4!1sDXCMr2ZoatlheaOlU-TI2g!2e0!7i13312!8i6656',
    'IV ЕГ': 'https://www.google.bg/maps/@43.2166186,27.9522045,3a,75y,335.76h,90t/data=!3m6!1e1!3m4!1sDXCMr2ZoatlheaOlU-TI2g!2e0!7i13312!8i6656',
    'lycee de langue francaise': 'https://www.google.bg/maps/@43.2166186,27.9522045,3a,75y,335.76h,90t/data=!3m6!1e1!3m4!1sDXCMr2ZoatlheaOlU-TI2g!2e0!7i13312!8i6656'
    }

# Choose your destination on Google maps
choice = 0
while choice not in range(1, 6):
    print('Cities in Bulgaria\n1. Sofia\n2. Plovdiv\n3. Stara Zagora\n4. Burgas\n5. Varna')
    print('Q for quit')
    choice = input('Your choice is: ')
    if choice == 'q' or choice == 'Q':
        sys.exit(0)
    try:
        choice = int(choice)  # Try to read as a number
    except:
        print('Not a number')

# Start point on Google maps
if choice == 1:
    location_on_map = BG_Sofia_map
elif choice == 2:
    location_on_map = BG_Plovdiv_map
elif choice == 3:
    location_on_map = BG_Stara_Zagora_map
elif choice == 4:
    location_on_map = BG_Burgas_map
elif choice == 5:
    # Select a random start point in Varna which is listed in the abouve defined dictionary.
    # Create flexible randomization function for selecting a start point.
    key_count = len(BG_Varna_map)
    key_list = list(BG_Varna_map.keys())
    index = random.randint(0, key_count - 1)
    key = key_list[index]
    location_on_map = BG_Varna_map[key]
else:
    print('Invalid choice. Exiting with error.')
    sys.exit(1)

# Variant 1 open the web browser
# subprocess.Popen([browser,location_on_map])
# Variant 2 open the web browser
webbrowser.open_new(location_on_map)

# Wait for 10 sec till the web page is fully loaded
sleep(15)

# How to start browser in maximized window?
# For browsers linke Firefox, Chrome, Midori under Linux press F11
# For browsers linke Firefox, Chrome under Windows press F11
if os_platform == 'Linux' or os_platform == 'Windows':
    pyautogui.press('f11')

Xmax, Ymax = pyautogui.size()
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
    pyautogui.moveTo(0.5*Xmax, (5/8.0)*Ymax, duration=1)
    pyautogui.click()
    time.sleep(1.5)


# Written by Pavlin Georgiev
# November 2015
# Last update: 5 March 2018
