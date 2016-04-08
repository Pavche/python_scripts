# Suppose that GNOME control center is running
# /usr/bin/gnome-control-center for RHEL7
# echo $(which gnome-control-center) for other Linux distributions

from dogtail.rawinput import *
from dogtail.tree import *
from time import sleep
from subprocess import *

# Start GNOME control center
p = Popen('/usr/bin/gnome-control-center')
sleep(3)

# Application instance of GNOME control center
app = root.application('gnome-control-center')
frame = app.child('Settings')
panel = frame.child('Hardware', roleName='panel')
sound_ico = panel.findChildren(lambda x: x.roleName=='icon' and x.text=='Sound')[0]  # Sound icon
sound_ico.click()
sleep(1)

sound_frame = app.child('Sound') # Sound settings
output_tab = sound_frame.child('Output', roleName='page tab')
output_tab.click()
sleep(1)

# List of sound output devices
sound_device_table = output_tab.findChildren(lambda x: x.roleName=='table cell')[0]
# Select a sound device byname
sound_device = sound_device_table.findChildren(lambda x : x.name=='Speakers - Built-in Audio')[0]
# Another possibility
#sound_device = sound_device_table.findChildren(lambda x : x.name=='Headphones - Built-in Audio')[0]
# Select a specific sound device
#sound_device = sound_device_table.findChildren(lambda x : x.name=='Headphones - Logitech USB Headset')[0]

sound_device.click()
sleep(1)

input_tab = sound_frame.child(name='Input',roleName='page tab')
input_tab.click()
sleep(1)

# List of sound input devices
sound_device_table = input_tab.findChildren(lambda x: x.roleName=='table cell')[0]
# Select the default device for sound input
sound_device = sound_device_table.findChildren(lambda x : x.name=='Internal Microphone - Built-in Audio')[0]
# Select a specific sound device
#sound_device = sound_device_table.findChildren(lambda x : x.name=='Microphone - Logitech USB Headset')[0]
sound_device.click()
sleep(1)

# Author: Pavlin Georgiev
# 1 April 2016