from urllib import request
import re

response = request.urlopen("https://morvanzhou.github.io/static/scraping/basic-structure.html").read().decode('utf-8')

res = re.findall(r'href="(.*?)"', response)
print("\nPage url is: ", res)
