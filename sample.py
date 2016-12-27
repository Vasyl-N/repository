from time import sleep
import pytest
from selenium import webdriver
import random
import string

email = ""
pw = ""
import json

def test_reg():

    regurl = "https://v2.whil.blue/sponsor/tml"
    mailurl = "http://email-fake.com/yopmail.pp.ua/"
    maildriver = webdriver.Chrome()
    #driver = webdriver.Chrome()
    maildriver.get(mailurl)
    email = maildriver.find_element_by_id("email_ch_text").text
    # driver.get(regurl)
    # driver.implicitly_wait(6)
    # driver.find_element_by_name("email").send_keys(email)
    # driver.find_element_by_name("first").send_keys(''.join(random.choice(string.lowercase) for i in range(20)))
    # driver.find_element_by_name("last").send_keys(''.join(random.choice(string.lowercase) for i in range(20)))
    # sleep(1)
    pw = "Passw0rd!"
    # driver.find_element_by_name("password").send_keys(pw)
    # driver.find_element_by_name("passwordAgain").send_keys(pw)

    with open("credentials.json", "r") as f:
        a = json.load(f)
    a[email] = pw
    print a
    with open('credentials.json', "w") as d:
        json.dump(a, d, indent=4)