from time import sleep
import testMethods as t
import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select



def test_if_user_is_logged_in():
    driver = webdriver.Chrome()
    driver.get("https://v2.whil.blue/home")


    email = "okumura81@yopmail.pp.ua"
    pw = "Passw0rd!"
    if t.isElementPresent(driver, "//header/span[contains(text(),'Welcome')]"):
        sleep(2)
        driver.find_element_by_partial_link_text("Exit").click()
    else:
        t.login(driver, email, pw)
        sleep(3)
        driver.find_element_by_partial_link_text("Exit").click()
        sleep(1)
        driver.find_element_by_xpath("//img[@alt='Activate WhilPower']").click()
        sleep(2)
