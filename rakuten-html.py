from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome import service as fs
from bs4 import BeautifulSoup
import time
from datetime import datetime,timezone,timedelta
import pytz

search = 'ダイエット'
itemWord = 'スラミー /Slamee'
shopWord = 'イコリス オンラインショップ'

driver_path = '/app/.chromedriver/bin/chromedriver'
chrome_service = fs.Service(executable_path=driver_path)
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=chrome_service, options=options)

ranking = []
for i in range(3):
	num = i + 1
	driver.get('https://search.rakuten.co.jp/search/mall/' + search + '/?p=' + str(num))
	html = driver.page_source
	soup = BeautifulSoup(html, 'html.parser')
	for item in soup.find_all(class_='searchresultitem'):
		for shopLink in item.find_all(class_='content merchant _ellipsis'):
			shopName = shopLink.text
		for itemtitle in item.find_all(class_='content title'):
			itemName = itemtitle.text
			if '[PR]' in itemName:
				continue
			shop = []
			shop.append(shopName)
			shop.append(itemName)
			ranking.append(shop)
	time.sleep(1)

del ranking[100:]

dt_now = datetime.now(pytz.timezone('Asia/Tokyo'))
dt_now = dt_now.strftime('%Y年%m月%d日')

print(dt_now)
print('順位：')

rankin = 'no'
for i in range(100):
	if shopWord in ranking[i][0]:
		if itemWord in ranking[i][1]:
			print(str(i + 1) + '位')
			rankin = 'yes'

if rankin == 'no':
	print('圏外')
