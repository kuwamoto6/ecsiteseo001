from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome import service as fs
from bs4 import BeautifulSoup
import time
from datetime import datetime,timezone,timedelta
import pytz

search = 'ダイエット'
itemWord = 'Slamee（スラミー）'
shopWord = 'イコリスオンラインショップ'

driver_path = '/app/.chromedriver/bin/chromedriver'
chrome_service = fs.Service(executable_path=driver_path)
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=chrome_service, options=options)

ranking = []
for i in range(3):
	num = 1
	num += i * 30
	driver.get('https://shopping.yahoo.co.jp/search?p=' + search + '&b=' + str(num))
	html = driver.page_source
	soup = BeautifulSoup(html, 'html.parser')
	for item in soup.find_all(class_='LoopList__item'):
		if '<p class="NmvwIc_82fYk _2bmFQDBQLBHN">PR</p>' in item:
			continue
		for shopLink in item.find_all(class_='ksNImwO9Q9LH'):
			shopName = shopLink.text
		for itemtitle in item.find_all(class_='WeRPqEQO_DMj'):
			itemName = itemtitle.text
		shop = []
		shop.append(shopName)
		shop.append(itemName)
		ranking.append(shop)
	time.sleep(1)

del ranking[100:]

dt_now = datetime.now(pytz.timezone('Asia/Tokyo'))
dt_now = dt_now.strftime('%Y/%m/%d')

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
