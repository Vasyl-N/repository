import re
import urllib
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
    f = urllib.urlopen("http://whil.com")
    s = f.read()
    f.close()

    # driver = webdriver.Chrome()
    result = re.match("(http|https)://[\w\-]+(\.[\w\-]+)+\S*", s)
    print result

    # draggable_element = driver.find_element_by_css_selector("svg > circle:nth-of-type(2)")
    # print draggable_element.location
    # actions = ActionChains(driver)
    # x = random.randint(-80, 80)
    # y = random.randint(0, 170)
    # actions.drag_and_drop_by_offset(draggable_element, x, 170)
    # actions.perform()
