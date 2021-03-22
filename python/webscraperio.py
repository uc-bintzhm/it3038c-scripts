import requests, re 
from bs4 import BeautifulSoup 
from urllib.request import urlopen
page = urlopen("https://en.wikipedia.org/wiki/Wingstop")

r = requests.get("https://en.wikipedia.org/wiki/Wingstop").content 

soup = BeautifulSoup(r, 'html.parser') 

html_bytes = page.read()
html = html_bytes.decode("utf-8")

d = soup.find("span", {"class":"toctext"})

print("A heading for this site is " + d.string + ".")
