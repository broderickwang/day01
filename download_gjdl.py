from bs4 import BeautifulSoup
import requests

URL = "http://www.nationalgeographic.com.cn/animals/"

html = requests.get(URL).text
soup = BeautifulSoup(html,"html.parser")

img_url = soup.find_all('div',{"class":"sec_oneimg cf"})

for ul in img_url:
    imgs = ul.find_all("img")
    for img in imgs:
        url = img['src']
        print("url is %s"%url)
        r = requests.get(url,stream=True)
        image_name=url.split('/')[-1]
        with open("./img/%s"% image_name,'wb') as f:
            for chunk in r.iter_content(chunk_size=128):
                f.write(chunk)
                print('Save as %s'%image_name)