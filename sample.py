import random
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains

import testMethods as t
driver = webdriver.Chrome()
email = "okumura81@yopmail.pp.ua"
password = "Passw0rd!"
# def test_ff():
t.login(driver, email, password)
sleep(1)
driver.get("https://v2.whil.blue/onboarding/age")

draggable_element = driver.find_element_by_css_selector("svg > circle:nth-of-type(2)")
actions = ActionChains(driver)
x = random.randint(-80, 80)
y = random.randint(0, 170)
actions.drag_and_drop_by_offset(draggable_element, x, y)
actions.perform()

t.selectMonth(driver)