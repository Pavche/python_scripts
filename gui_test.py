from time import time,sleep
from selenium import webdriver

# get initial window size
driver = webdriver.Firefox()
print driver.get_window_size()

sleep(5)

# set window size
driver.set_window_size(480, 320)
print driver.get_window_size()

sleep(5)

# maximize window
driver.maximize_window()
print driver.get_window_size()

sleep(5)

driver.quit()
