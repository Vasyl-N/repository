import pytest
from selenium import webdriver
import requests
from selenium.webdriver.common.keys import Keys
import webbrowser
import urllib2
import re

@pytest.fixture()


def src_find(page):
    wd.get(page)
    src_lst = []
    lst = wd.find_elements_by_tag_name("*")
    for i in lst:
        if hasattr(i, "src"):
            src_lst.extend(i)
    return src_lst

def Test_HTTP_code(i):
        r = requests.head(i.get_attribute("href")).status_code
        print i.get_attribute("href")
        print r
        if r >= 200 and r<400:
            print "Test Pass"
        else:
            print "Test Fail.Test Fail.Test Fail.Test Fail.Test Fail.Test Fail.Test Fail.Test Fail.Test Fail.Test Fail.Test Fail"

def Test_HTTP_code_SRC(i):
            s = requests.head(i.get_property("currentSrc")).status_code
            print i.get_property("currentSrc")
            print s
            if s == 200:
                print "SRC_Test Pass"
            else:
                print "SRC_Test Fail.SRC_Test Fail.SRC_Test Fail.SRC_Test Fail.SRC_Test Fail.SRC_Test Fail.SRC_Test Fail.SRC_Test Fail"


wd= webdriver.Chrome()


def login(url):
    wd.get(url)
    Email = wd.find_element_by_name("email")
    Email.send_keys(username)
    Pass = wd.find_element_by_name("password")
    Pass.send_keys(password)
    wd.find_element_by_xpath(".//*[@id='login']/div[2]/footer[2]/div[1]/button").click()
    wd.implicitly_wait(5)
    wd.find_element_by_xpath("html/body/div[5]/div/div[5]/a[1]").click() #closes coaching tips



Web_Pages = ["https://v2.whil.blue/home","https://v2.whil.blue/programs/subjects?program=thrive","https://v2.whil.blue/programs/subjects?program=lead",
             "https://v2.whil.blue/programs/subjects?program=move", "https://v2.whil.blue/whilpower/category",
             "https://v2.whil.blue/goals?category=health", "https://v2.whil.blue/goals?category=performance",
             "https://v2.whil.blue/goals?category=relationships", "https://v2.whil.blue/settings", ]


username = "achraftom1mot1@yopmail.pp.ua"  #Change username Here
password = "Passw0rd!" #Change Password here
url = "https://v2.whil.blue" #Change URL here
login(url)


for page in Web_Pages:
    wd.get(page)
    print "________", page, "_________"
    lst = wd.find_elements_by_xpath("//*[@href]")

    for i in lst:
        Test_HTTP_code(i)
    src = wd.find_elements_by_tag_name("*")
    for i in src:
        if i.get_property("currentSrc") == None:
            pass
        else:
            Test_HTTP_code_SRC(i)



wd.quit()
