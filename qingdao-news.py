from bs4 import BeautifulSoup
import requests

# 青岛新闻网
URL = "http://www.qingdaonews.com/"

html = requests.get(URL)
html.encoding='utf-8'
# print(html.text)
# print("html is : "+html.text)
soup = BeautifulSoup(html.text,"html.parser")

urls = soup.find_all('ul',{"class":"newsList"})

for url in urls:
    # print(url)
    hrefs = url.find_all("a")
    for href in hrefs:
        h = href['href']
        news_page = requests.get(h)
        news_page.encoding='utf-8'
        news_soup = BeautifulSoup(news_page.text,"html.parser")

        # 获取标题
        titles = news_soup.find_all('h1',{'class':'m-tt-1'})
        for title in titles:
            print(title)

        # 获取来源，发布时间
        fromDivs = news_soup.find_all('div',{'class':'m-msg-1'})
        for fromdiv in fromDivs:
            spans = fromdiv.find_all('span')
            for span in spans:
                print(span)

        # 获取文章内容
        divs = news_soup.find_all('div',{'class':'m-ct mb80'})
        for div in divs:
            print(div)
