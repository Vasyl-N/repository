from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

regurl = "https://v2.whil.blue/sponsor/tml"
#regurl = "https://connect.whil.com/sponsor/tml"
driver = webdriver.Chrome()
driver.get(regurl)

def test_validform():
    driver.find_element_by_name("email").send_keys(Keys.TAB)
    driver.find_element_by_name("first").send_keys(Keys.TAB)
    driver.find_element_by_name("last").send_keys(Keys.TAB)
    pw = "Passw0rd!"
    driver.find_element_by_name("password").send_keys()
    driver.find_element_by_name("passwordAgain").send_keys(pw)

    emaildanger = driver.find_element_by_xpath("//*[@name='email']/following-sibling::span").text
    assert emaildanger == "An email is required", "Wrong email error text"

    driver.find_element_by_name("email").send_keys("dsdsd", Keys.TAB)
    withoutat = driver.find_element_by_xpath("//*[@name='email']/following-sibling::span").text
    assert withoutat == "Invalid email. Missing '@' Missing '.'", "Wrong Assert @ Sign"

    firstdanger = driver.find_element_by_xpath("//*[@name='first']/following-sibling::span").text
    assert firstdanger == "Required", "Wrong First Name Error Message"

    lastdanger = driver.find_element_by_xpath("//*[@name='last']/following-sibling::span").text
    assert lastdanger == "Required", "Wrong Last Name Error Message"

    emptyPass = driver.find_element_by_xpath(".//*[@name='password']/following-sibling::span").text
    assert emptyPass == "Required, at least 8 characters", "Wrong empty password message"



#validform()
driver.quit()