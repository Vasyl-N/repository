import urllib
from selenium import webdriver
from bs4 import BeautifulSoup, BeautifulStoneSoup
import urllib2
import re
import requests
def test_bla()

    f = urllib.urlopen("http://whil.com")
    s = f.read()
    f.close()

    # driver = webdriver.Chrome()
    urls = "https?:\/\/(?:www\.|(?!www))[^\s\.]+\.[^\s]{2,}|www\.[^\s]+\.[^\s]{2,}"
    result = re.match(urls, s)
    print result

    #
    # soup = BeautifulSoup(s)
    # inputTag = soup.findAll(attrs={"name": "stainfo"})
    # output = inputTag[0]['value']
    # print output
    #
    # r = requests.get("http://whil.com")
    # print r.status_code
