from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

regurl = "https://v2.whil.blue/sponsor/tml"
#regurl = "https://connect.whil.com/sponsor/tml"

driver = webdriver.Chrome()
def test_login():
    driver.implicitly_wait(2)
    driver.get("https://v2.whil.blue")

    with open("mails.rtf") as f:
        content = f.readlines()
    for i in content:
        driver.get("https://v2.whil.blue")
        i = i[:-1]
        driver.find_element_by_name("email").send_keys(i)
        driver.find_element_by_name("password").send_keys("Passw0rd!", Keys.ENTER)
        sleep(2)
        #driver.find_element_by_xpath("//header/span[contains(text(),'Welcome')]")
        #assert driver.current_url == "https://v2.whil.blue/onboarding"
        #if driver.find_element_by_xpath("//header/span[contains(text(),'Welcome')]"):
        print i + driver.current_url