from bs4 import BeautifulSoup
import requests

# 青岛新闻网
URL = "https://www.toutiao.com/"

headers = {
    'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}

html = requests.get(url=URL,headers=headers)
html.encoding='utf-8'
print(html.text)