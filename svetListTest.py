import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_links(driver):
    driver.get("https://www.whil.com/")
    links = len(driver.find_elements_by_css_selector("div.scroll li"))
    text = ""

    while links > 0:
        driver.find_element_by_css_selector("div.scroll li:nth-of-type(%d)" % links).click()
        new_text = driver.find_element_by_css_selector("div.slider-content h1").text

        if text == new_text:
            raise StandardError ("Ha! Wrong text. Same text on 2 diff pages in %s, %s" % (text, new_text))
        else:
            text = new_text
        print "Text changed to ", new_text
        links -= 1