#!/usr/bin/env python
# Python 3 program
# Copyright (c) 2023 Steve Barlow

"""Check every 5 minutes if there is any change on the stadt.muenchen.de page to book an appointment to transfer
a foreign driver's licence and alert if there is, meaning an appointment might be available."""

import sys
import os
import time
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from webdriver_manager.chrome import ChromeDriverManager

POLL_INTERVAL = 5 # In minutes

def appt_page():
    """Open the appointment page and return the HTML of the appointment table.
    This is the top level function called by the main code.
    """

    # Keep going if we don't succeed the first time
    while True:
        try:
            driver.get('https://stadt.muenchen.de/terminvereinbarung_/terminvereinbarung_fs.html?&loc=FS&ct=1071898')
            time.sleep(3)
            iframe = driver.find_element(By.XPATH, '//iframe[@id="appointment"]')
            driver.switch_to.frame(iframe)
            button = driver.find_element(By.XPATH, '//input[@value="Weiter"]')
            button.click()
            time.sleep(3)
            appt_info = driver.find_element(By.CLASS_NAME, 'WEBAPPOINT_LOCATION_CONTENT')
            html = appt_info.get_attribute('innerHTML')
            return html
        except:
            pass

def sound_alert():
    """Play a repeating alert sound, blocking while the sound is playing."""
    for i in range(10):
        os.system('afplay /System/Library/Sounds/Sosumi.aiff')
        time.sleep(1)


# ---------------------------------------------------------------------------------------
# Main code

options = webdriver.ChromeOptions()
options.add_argument('--window-size=990,1100')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.execute_cdp_cmd('Network.setCacheDisabled', {'cacheDisabled':True})

print('Doing initial read')
initial_html = appt_page()
print('Now polling every {} minutes'.format(POLL_INTERVAL))

while True:
    time.sleep(POLL_INTERVAL * 60)
    tnow = datetime.datetime.now()
    t = tnow.strftime('%Y-%m-%d %H:%M:%S')
    
    html = appt_page()
    if html == initial_html:
        print(t, ':', 'Unchanged')
    else:
        print(t, ':', 'Appointments updated')
        # Done as a 'try' as fails if display has gone into standby
        try:
            sound_alert()
        except:
            pass
        # Leave the browser open so you can manually make an appointment...
        input('Manually make appointment in browser window. Press return to exit. ')
        sys.exit(0)
