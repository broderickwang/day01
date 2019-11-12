from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen("https://morvanzhou.github.io/static/scraping/list.html").read().decode('utf-8')
print(html)

soup = BeautifulSoup(html,'html.parser')

month = soup.find_all('li',{"class":"month"})
for m in month:
    print(m.get_text())

jian = soup.find('ul',{"class":"jan"})
d_jan = jian.find_all('li')
for d in d_jan:
    print(d.get_text())