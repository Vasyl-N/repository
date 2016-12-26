import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


regurl = "https://v2.whil.blue/sponsor/tml"
#regurl = "https://connect.whil.com/sponsor/tml"



@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_validform(driver):
    driver.get(regurl)
    driver.find_element_by_name("email").send_keys(Keys.TAB)
    driver.find_element_by_name("first").send_keys(Keys.TAB)
    driver.find_element_by_name("last").send_keys(Keys.TAB)
    pw = "Passw0rd!"
    driver.find_element_by_name("password").send_keys(Keys.TAB)
    driver.find_element_by_name("passwordAgain").send_keys(Keys.TAB)

    emaildanger = driver.find_element_by_xpath("//div[contains(@class, 'form-group') and .//input[@name='email']]//span[@class='text-danger' and text()!=0]").text
    assert emaildanger == "An email is required", "Wrong email error text"

    driver.find_element_by_name("email").send_keys("dsdfdfdsd", Keys.TAB)
    withoutat = driver.find_element_by_xpath("//div[contains(@class, 'form-group') and .//input[@name='email']]//span[@class='text-danger' and text()!=0]").text
    assert withoutat == "Invalid email. Missing '@' Missing '.'", "Wrong Assert @ Sign"

    firstdanger = driver.find_element_by_xpath("//div[contains(@class, 'form-group') and .//input[@name='first']]//span[@class='text-danger' and text()!=0]").text
    assert firstdanger == "Required", "Wrong First Name Error Message"

    lastdanger = driver.find_element_by_xpath("//div[contains(@class, 'form-group') and .//input[@name='last']]//span[@class='text-danger' and text()!=0]").text
    assert lastdanger == "Required", "Wrong Last Name Error Message"

    emptyPass = driver.find_element_by_xpath("//div[contains(@class, 'form-group') and .//input[@name='password']]//span[@class='text-danger' and text()!=0]").text
    assert emptyPass == "Required, at least 8 characters", "Wrong empty password message"

    driver.find_element_by_name("password").send_keys("bla bla bla")
    onlyletters = driver.find_element_by_xpath("//div[contains(@class, 'form-group') and .//input[@name='password']]//span[@class='text-danger' and text()!=0]").text
    assert onlyletters == "Must have at least one number", "Wrong empty password message"

    driver.find_element_by_name("password").clear()
    driver.find_element_by_name("password").send_keys("Blablabla43")
    nopunctuation = driver.find_element_by_xpath("//div[contains(@class, 'form-group') and .//input[@name='password']]//span[@class='text-danger' and text()!=0]").text
    assert nopunctuation == "Use at least one punctuation", "Wrong empty password message"

    driver.find_element_by_name("password").clear()
    driver.find_element_by_name("password").send_keys("bla bla bla43")

    nouppercase = driver.find_element_by_xpath("//div[contains(@class, 'form-group') and .//input[@name='password']]//span[@class='text-danger' and text()!=0]").text
    assert nouppercase == "Use at least one uppercase character", "Wrong empty password message"


    emptyPassAgain = driver.find_element_by_xpath("//div[contains(@class, 'form-group') and .//input[@name='passwordAgain']]//span[@class='text-danger' and text()!=0]").text
    assert emptyPassAgain == "Required", "Wrong empty passwordAgain  message"

    driver.find_element_by_xpath("//button/span[text()='JOIN']").click()

    assert driver.current_url == regurl
