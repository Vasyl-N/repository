from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def test_mem_set():
    driver = webdriver.Chrome()
    driver.implicitly_wait(6)
    driver.get("https://v2.whil.blue")

    driver.find_element_by_name("email").send_keys("okumura81@yopmail.pp.ua")
    driver.find_element_by_name("password").send_keys("Passw0rd!", Keys.ENTER)

    # for i in range(5):
    #     sleep(1)
    #     driver.find_element_by_partial_link_text("Next").click()
    driver.find_element_by_partial_link_text("Exit").click()
    sleep(2)

    ms = driver.find_element_by_xpath('//a[@href="/settings"]')
    ms.click()
    sleep(2)

    links = driver.find_elements_by_xpath("//a[@aria-label='menu item']")
    links = links[1:-1]

    for i in links:
        url = driver.current_url
        print i.text
        i.click()
        sleep(1)
        assert url != driver.current_url

