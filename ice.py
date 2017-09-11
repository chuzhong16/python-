import requests 
from bs4 import BeautifulSoup
import time 

def savePic(url,name):
	#fill the cookie
	headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36',
	'Cookie':r'__cfduid=d831dc19ecc3c132a03fc848fb27e169a1481366710; MoodleSessionice2016=fueidh8ee7kd91mhinjqgja1l7; _pk_ref.8.cbe1=%5B%22%22%2C%22%22%2C1503295780%2C%22http%3A%2F%2Fguide.xjtlu.edu.cn%2F%22%5D; _pk_id.8.cbe1=3f2bfb75909fba73.1480758454.88.1503295844.1503295780.; _ga=GA1.3.359625663.1480921280; _gid=GA1.3.519371222.1504859030; MoodleSessionice2017=kall71ep1q89m0ntkqralbi1f4'}
	root = "/Users/mac/Desktop/xjtlu/照片/"
	path = root + name + '.jpg'
	r = requests.get(url,headers=headers)
	with open (path,"wb") as f:
		f.write(r.content)
	f.close()

def findPic(url):
	#fill the cookie
	headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36',
	'Cookie':r'__cfduid=d831dc19ecc3c132a03fc848fb27e169a1481366710; MoodleSessionice2016=fueidh8ee7kd91mhinjqgja1l7; _pk_ref.8.cbe1=%5B%22%22%2C%22%22%2C1503295780%2C%22http%3A%2F%2Fguide.xjtlu.edu.cn%2F%22%5D; _pk_id.8.cbe1=3f2bfb75909fba73.1480758454.88.1503295844.1503295780.; _ga=GA1.3.359625663.1480921280; _gid=GA1.3.519371222.1504859030; MoodleSessionice2017=kall71ep1q89m0ntkqralbi1f4'}
	
	wb_data = requests.get(url,headers = headers)
	#time.sleep(2)  #To slow down the crawler
	soup = BeautifulSoup(wb_data.text,'lxml')
	
	try:
		imgs = soup.select('img[width="100"]') 
		for img in imgs: 
			name = img.get("alt").split('of')[-1] #get the students' names
			savePic(img.get("src"),name)
			#lis.append(img.get("src"))
			print("success!"+ name)

	except:
		print("failure")

urls = ['http://ice.xjtlu.edu.cn/user/profile.php?id={}'.format(str(i)) for i in range (19999,20000)]
for url in urls:
	findPic(url)