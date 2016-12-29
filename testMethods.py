from time import sleep
import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random
import string
from selenium.webdriver.support.wait import WebDriverWait
import json


# class tests():
def setWDInstanse():
    driver = webdriver.Chrome()
    driver.implicitly_wait(6)
    return driver


def setMailDriver():
    maildriver = webdriver.Chrome()
    return maildriver


def setTestURL():
    regurl = "https://v2.whil.blue/sponsor/tml"
    return regurl


def setMailUrl():
    mailurl = "http://email-fake.com/yopmail.pp.ua/"
    return mailurl


def getRegURL(regurl, driver):
    driver.get(regurl)


def getMailURL(mailurl, maildriver):
    maildriver.get(mailurl)


def getEmail(maildriver):
    email = maildriver.find_element_by_id("email_ch_text").text
    return email


def typeEmail(driver, email):
    driver.find_element_by_name("email").send_keys(email)


def randomStr():
    return ''.join(random.choice(string.lowercase) for i in range(20))


def typeFirst(driver, ranStr):
    driver.find_element_by_name("first").send_keys(ranStr)


def typeLast(driver, ranStr):
    driver.find_element_by_name("last").send_keys(ranStr)


def selectCity(driver):
    arr = []
    for i in driver.find_elements_by_xpath("//select[@name='requestPartyJoin.questionAnswers.1']/option"):
        arr.append(i.text)
    arr = arr[1:]
    Select(driver.find_element_by_name("requestPartyJoin.questionAnswers.1")).select_by_visible_text(random.choice(arr))


def selectExperience(driver):
    arr = []
    for i in driver.find_elements_by_xpath("//select[@name='requestPartyJoin.questionAnswers.2']/option"):
        arr.append(i.text)
    arr = arr[1:]
    Select(driver.find_element_by_name("requestPartyJoin.questionAnswers.2")).select_by_visible_text(random.choice(arr))


def getPassword():
    pw = "Passw0rd!"
    return pw


def typePassword(driver, pw):
    driver.find_element_by_name("password").send_keys(pw)
    driver.find_element_by_name("passwordAgain").send_keys(pw)


def writeCredentials(email, pw):
    with open("credentials.json", "r") as f:
        a = json.load(f)
    a[email] = pw
    with open('credentials.json', "w") as d:
        json.dump(a, d, indent=4)


# def writeEmailToFile(email):
#     file = open("mails.rtf", "a")
#     file.writelines(email + '\n')
#     file.close()
def clickJoin(driver):
    driver.find_element_by_xpath("//button/span[text()='JOIN']").click()


def verifyEmail(maildriver):
    try:
        WebDriverWait(maildriver, 100).until(
            EC.presence_of_element_located((By.XPATH, '//a[text()="Verify my email address"]')))
    finally:
        maildriver.find_element_by_xpath('//a[text()="Verify my email address"]').click()
        sleep(2)


def login(driver, email, pw):
    driver.get("https://v2.whil.blue")
    driver.find_element_by_name("email").send_keys(email)
    driver.find_element_by_name("password").send_keys(pw, Keys.ENTER)


def chooseGender(driver):
    sleep(1)
    arr = driver.find_elements_by_xpath(
        "//div[@class='center-block']/div/div[.//span and .//img] | //button[@type='submit']")
    l = arr[random.randint(0, len(arr) - 1)]
    l.click()
    sleep(2)


def setAge(driver):
    draggable_element = driver.find_element_by_css_selector("svg > circle:nth-of-type(2)")
    actions = ActionChains(driver)
    x = random.randint(-80, 80)
    y = random.randint(0, 170)
    actions.drag_and_drop_by_offset(draggable_element, x, y)
    actions.perform()


def selectMonth(driver):
    textarr = []
    for i in driver.find_elements_by_xpath("//select[@name='monthSelect']/option"):
        textarr.append(i.text)
    Select(driver.find_element_by_xpath("//select[@name='monthSelect']")).select_by_visible_text(random.choice(textarr))
    driver.find_element_by_xpath("//button[text()='Next']").click()


def selectEXP(driver):
    sleep(1)
    arr = driver.find_elements_by_xpath("//div[@class='col-xs-4']")
    arr[random.randint(0, len(arr) - 1)].click()
    sleep(5)


def userTips(driver):
    for i in range(5):
        sleep(1)
        driver.find_element_by_partial_link_text("Next").click()
    driver.find_element_by_partial_link_text("Done").click()


def isElementPresent(driver, locator):
    try:
        driver.find_element_by_xpath(locator)
    except NoSuchElementException:
        return False
    return True

def wait_for_any_new_window(driver, old_windows, seconds):
    WebDriverWait(driver, seconds).until(
        lambda driver: old_windows != driver.window_handles)