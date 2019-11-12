from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen("https://morvanzhou.github.io/static/scraping/basic-structure.html").read().decode('utf-8')
# soup = BeautifulSoup(html, features='lxml')

soup = BeautifulSoup(html, 'html.parser')
# soup = BeautifulSoup(html, "lxml")
print(soup.h1)
print(soup.p)
print(soup.image)
