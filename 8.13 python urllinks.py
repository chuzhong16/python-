import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl
url=input('Enter-')
html=urllib.request.urlopen(url).read()
soup=BeautifulSoup(html,'html.parser')
for tag in tags:
	print(tag.get('href',None))
