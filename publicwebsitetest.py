from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def test_mem_set():
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.get("https://www.whil.com/index.html")
    links = driver.find_elements_by_xpath('//nav[@class="main-nav text-xs-right"]/ul/li')
    linktext = []
    for i in links:
        linktext.append(i.text)
    h1 = ""
    for i in linktext:
        driver.find_element_by_link_text(i).click()
        assert h1 != driver.find_element_by_xpath("//*[@id='slider-1']/div[1]/div/h1").text
        h1 = driver.find_element_by_xpath("//*[@id='slider-1']/div[1]/div/h1").text
        print h1