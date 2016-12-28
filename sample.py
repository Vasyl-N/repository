from time import sleep
import pytest
from selenium import webdriver
import random
import string

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

email = ""
pw = ""
import json


def test_reg():
    regurl = "https://v2.whil.blue"
    driver = webdriver.Chrome()
    driver.get(regurl)
    driver.implicitly_wait(6)
    driver.find_element_by_name("email").send_keys("safmohamed@yopmail.pp.ua")
    driver.find_element_by_name("password").send_keys("Passw0rd!", Keys.ENTER)
    sleep(2)
    driver.get("https://v2.whil.blue/onboarding/gender")
    sleep(2)
    arr = driver.find_elements_by_xpath("//div[@class='center-block']/div/div[.//span and .//img] | //button[@type='submit']")
    print arr
    # l = arr[random.randint(0, len(arr) - 1)]
    arr[1].click()
    sleep(3)
    # l.click()


    #
    # draggable_element = driver.find_element_by_css_selector("svg > circle:nth-of-type(2)")
    # print draggable_element.location
    # actions = ActionChains(driver)
    # x = random.randint(-80, 80)
    # y = random.randint(0, 170)
    # actions.drag_and_drop_by_offset(draggable_element, x, 170)
    # actions.perform()
