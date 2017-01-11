
import testMethods as t
from selenium import webdriver
def test_tip():
    driver = webdriver.Chrome()
    email = "okumura81@yopmail.pp.ua"
    password = "Passw0rd!"
    t.login(driver, email, password)
