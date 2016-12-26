import pytest
from time import sleep, time
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import random
from random import randint


def test_reg():
    driver = webdriver.Chrome()

    # driver.get("https://v2.whil.blue/onboarding/gender")
    driver.get("https://v2.whil.blue/sponsor/tml")

    arr = []
    for i in driver.find_elements_by_xpath("//select[@name='requestPartyJoin.questionAnswers.2']/option"):
        arr.append(i.text)
    arr = arr[1:]
    Select(driver.find_element_by_name("requestPartyJoin.questionAnswers.2")).select_by_visible_text(random.choice(arr))
    print arr