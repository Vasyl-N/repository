from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://www.ebay.com/rpp/vehicles")

links = driver.find_elements_by_xpath("//ul[@class='navigation-list nested']//a[@class='title extended-links']")
print str(links)
for i in links:
    print i.text


driver.quit()

