from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

import ast

from selenium.webdriver.support.color import Color

driver = webdriver.Chrome()


def test_colors():
    driver.implicitly_wait(7)
    email = "okumura81@yopmail.pp.ua"
    pw = "Passw0rd!"
    driver.get("https://v2.whil.blue")
    driver.find_element_by_name("email").send_keys(email)
    driver.find_element_by_name("password").send_keys(pw, Keys.ENTER)
    sleep(4)
    driver.find_element_by_partial_link_text('Exit').click()
    sleep(1)

    driver.find_element_by_xpath("//div[text()='Health']").click()




    rgb1 = driver.find_element_by_xpath(
        '//div[@class="src-containers-goals-___styles__goalsHeader___1VP2m"]').value_of_css_property("background-color")
    hex1 = Color.from_string(rgb1).hex
    driver.back()
    sleep(2)
    driver.find_element_by_xpath("//div[text()='Performance']").click()
    rgb2 = driver.find_element_by_xpath(
        '//div[@class="src-containers-goals-___styles__goalsHeader___1VP2m"]').value_of_css_property("background-color")
    hex2 = Color.from_string(rgb2).hex
    driver.back()
    sleep(2)
    driver.find_element_by_xpath("//div[text()='Relationships']").click()
    rgb3 = driver.find_element_by_xpath(
        '//div[@class="src-containers-goals-___styles__goalsHeader___1VP2m"]').value_of_css_property("background-color")
    hex3 = Color.from_string(rgb3).hex

    assert hex1 == "#30a064"
    assert hex2 == "#475d6f"
    assert hex3 == "#ffab20"