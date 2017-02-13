from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json

regurl = "https://v2.whil.blue/sponsor/tml"

def test_login():
    driver = webdriver.Firefox()
    driver.get("https://v2.whil.blue")
    with open("credentials.json") as f:
        a = json.load(f)
    for i in a.items():
        driver.get("https://v2.whil.blue")
        driver.find_element_by_name("email").send_keys(i[0])
        driver.find_element_by_name("password").send_keys(i[1], Keys.ENTER)
        sleep(1)
        url = driver.current_url
        if driver.current_url == "https://v2.whil.blue/":
            print("%s did NOT login" % i[0])
        elif driver.current_url == "https://v2.whil.blue/home":
            print("%s is logged in SUCCESSFULLY" % i[0])
        elif "https://v2.whil.blue/onboarding/" in driver.current_url:
            print("%s is on board" % i[0])
        else:
            print("%s - unknown url %s" % i([0], url))

    # with open("credentials.json", "r") as f:
    #     a = json.load(f)
    # a[email] = pw
    # with open('credentials.json', "w") as d:
    #     json.dump(a, d, indent=4 )