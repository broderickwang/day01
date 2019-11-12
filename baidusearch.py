import requests
import webbrowser

# param={"wd":"许桓彩"}
# r = requests.get("http://www.baidu.com/s",params=param)
# print(r.url)
# webbrowser.open(r.url)

data = {"firstname":"chengda","lastname":"wang"}

r = requests.post("http://pythonscraping.com/files/processing.php",data=data)
print(r.text)