import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#@pytest.fixture
# def driver(request):
#     wd = webdriver.Chrome()
#     request.addfinalizer(wd.quit)
#     return wd
from selenium.webdriver.support.wait import WebDriverWait

maildriver = webdriver.Chrome()
driver = webdriver.Chrome()

def test_reg():
    regurl = "https://v2.whil.blue/sponsor/tml"
    mailurl = "http://email-fake.com/yopmail.pp.ua/"
    maildriver = webdriver.Chrome()
    driver = webdriver.Chrome()
    maildriver.get(mailurl)
    email = maildriver.find_element_by_id("email_ch_text").text
    driver.get(regurl)
    driver.find_element_by_name("email").send_keys(email)
    driver.find_element_by_name("first").send_keys("Test")
    driver.find_element_by_name("last").send_keys("Test")
    select = Select(driver.find_element_by_name("requestPartyJoin.questionAnswers.1"))
    select.select_by_visible_text("London")
    select = Select(driver.find_element_by_name("requestPartyJoin.questionAnswers.2"))
    select.select_by_value("2,no")
    pw = "Passw0rd!"
    driver.find_element_by_name("password").send_keys(pw)
    driver.find_element_by_name("passwordAgain").send_keys(pw)

    driver.find_element_by_xpath("//button/span[text()='JOIN']").click()
    # def writemail():
    file = open("mails.rtf", "a")
    file.writelines(email + '\n')
    file.close()

    #wait = WebDriverWait(maildriver, 200)
    #element = wait.until(EC.presence_of_element_located((By.LINK_TEXT,'Verify my email address')))
    try:
        WebDriverWait(maildriver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//a[text()="Verify my email address"]'))
        )
    finally:
        print "bla bla"
        maildriver.find_element_by_xpath('//a[text()="Verify my email address"]').click()

