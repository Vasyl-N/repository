from bs4 import BeautifulSoup
import urllib2
import re
import requests

html_page = urllib2.urlopen("http://whil.com")
soup = BeautifulSoup(html_page)
links = []

for link in soup.findAll('a'):
    links.append(link.get('href'))
print(links)

for i in links:

    r = requests.get(i)
    print r.status_code
    print r.headers
    print r.content