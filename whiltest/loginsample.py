import pytest
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

driver.get("http://email-fake.com/yopmail.pp.ua/mr.lightlost")
try:
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH,'//a[text()="Verify my email address"]'))
    )
finally:
    print "bla bla"
    driver.find_element_by_xpath('//a[text()="Verify my email address"]').click()
