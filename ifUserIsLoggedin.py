from time import sleep
import testMethods as t
from selenium import webdriver


def test_if_user_is_logged_in():
    driver = webdriver.Chrome()
    driver.get("https://v2.whil.blue/home")

    email = "okumura81@yopmail.pp.ua"
    pw = "Passw0rd!"
    if not t.isElementPresent(driver, "//header/span[contains(text(),'Welcome')]"):
        t.login(driver, email, pw)
    sleep(1)
    driver.find_element_by_xpath("//img[@alt='Activate WhilPower']").click()