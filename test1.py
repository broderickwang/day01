import urlib2
response = urlib2.urlopen("http://www.baidu.com")
print (response.read())
