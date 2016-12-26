from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random

#@pytest.fixture
# def driver(request):
#     wd = webdriver.Chrome()
#     request.addfinalizer(wd.quit)
#     return wd
from selenium.webdriver.support.wait import WebDriverWait


email = ""
pw = ""
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

    arr = []
    for i in driver.find_elements_by_xpath("//select[@name='requestPartyJoin.questionAnswers.1']/option"):
        arr.append(i.text)
    arr = arr[1:]
    Select(driver.find_element_by_name("requestPartyJoin.questionAnswers.1")).select_by_visible_text(random.choice(arr))
    print arr
   #Select(driver.find_element_by_name("requestPartyJoin.questionAnswers.1")).select_by_visible_text("London")

    arr = []
    for i in driver.find_elements_by_xpath("//select[@name='requestPartyJoin.questionAnswers.2']/option"):
        arr.append(i.text)
    arr = arr[1:]
    Select(driver.find_element_by_name("requestPartyJoin.questionAnswers.2")).select_by_visible_text(random.choice(arr))
    print arr


    Select(driver.find_element_by_name("requestPartyJoin.questionAnswers.2")).select_by_value("2,no")
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
        WebDriverWait(maildriver, 100).until(EC.presence_of_element_located((By.XPATH, '//a[text()="Verify my email address"]')))
    finally:
        maildriver.find_element_by_xpath('//a[text()="Verify my email address"]').click()

#def test_reg():
#    driver = webdriver.Chrome()
    driver.implicitly_wait(6)

    driver.get("https://v2.whil.blue")
    driver.find_element_by_name("email").send_keys(email)
    driver.find_element_by_name("password").send_keys("Passw0rd!", Keys.ENTER)


    arr = []
    male = (driver.find_element_by_xpath("//*[@data-value='Male']"))
    arr.append(male)
    female = (driver.find_element_by_xpath("//*[@data-value='Female']"))
    arr.append(female)
    other = (driver.find_element_by_xpath("//*[@data-value='Other']"))
    arr.append(other)
    skip = (driver.find_element_by_xpath("//*[@data-value='None']"))
    arr.append(skip)
    l = arr[random.randint(0, len(arr) - 1)]
    l.click()

    draggable_element = driver.find_element_by_css_selector("svg > circle:nth-of-type(2)")

    draggable_element.location
    actions = ActionChains(driver)
    x = random.randint(-60, 60)
    y = random.randint(0, 170)
    actions.drag_and_drop_by_offset(draggable_element, x, y)
    actions.perform()

    textarr = []
    for i in driver.find_elements_by_xpath("//select[@name='monthSelect']/option"):
        textarr.append(i.text)
    Select(driver.find_element_by_xpath("//select[@name='monthSelect']")).select_by_visible_text(random.choice(textarr))
    driver.find_element_by_xpath("//button[text()='Next']").click()

    arr = []
    male = (driver.find_element_by_xpath("//*[@data-value='Newbie']"))
    arr.append(male)
    female = (driver.find_element_by_xpath("//*[@data-value='Some Experience']"))
    arr.append(female)
    other = (driver.find_element_by_xpath("//*[@data-value='Expert']"))
    arr.append(other)
    l = arr[random.randint(0, len(arr) - 1)]
    l.click()
    sleep(5)
    for i in range(5):
        sleep(1)
        driver.find_element_by_partial_link_text("Next").click()
    driver.find_element_by_partial_link_text("Done").click()