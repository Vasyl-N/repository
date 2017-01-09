
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import testMethods as t
from selenium import webdriver
def test_two_windows():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 5)
    driver.get("http://whil.com")
    old_windows = driver.window_handles
    driver.find_element_by_xpath("//div[@class='row']/div[3]/a/img").click()
    t.wait_for_any_new_window(driver, old_windows, 5)
    driver.switch_to.window(driver.window_handles[1])
    wait.until(EC.text_to_be_present_in_element((By.XPATH, "//h1"), "Whil Concepts"))

    assert driver.find_element_by_xpath("//h1[@class='name']/span").text == "Whil Concepts"
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    a = driver.find_elements_by_xpath("html/body/div[1]/section/div[1]/a/img")
    if len(a) == 0:
        raise StandardError, "No element found:"
    #wait.until(EC.visibility_of_element_located((By.XPATH, "html/body/div[1]/section/div[1]/a/img")))