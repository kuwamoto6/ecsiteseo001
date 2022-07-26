from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome import service as fs
from bs4 import BeautifulSoup
import time
from datetime import datetime,timezone,timedelta
import pytz

search = 'ダイエット'
itemWord = 'Slamee スラミー'

driver_path = '/app/.chromedriver/bin/chromedriver'
chrome_service = fs.Service(executable_path=driver_path)
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=chrome_service, options=options)

ranking = []
for i in range(3):
	num = i + 1
	driver.get('https://www.amazon.co.jp/s?k=' + search + '&page=' + str(num))
	html = driver.page_source
	soup = BeautifulSoup(html, 'html.parser')
	for item in soup.find_all(class_='s-widget-spacing-small'):
		for itemtitle in item.find_all(class_='s-title-instructions-style'):
			itemName = itemtitle.text
			if 'スポンサースポンサー' in itemName:
				continue
			ranking.append(itemName)
	time.sleep(1)

del ranking[100:]

dt_now = datetime.now(pytz.timezone('Asia/Tokyo'))
dt_now = dt_now.strftime('%Y/%m/%d')

print(dt_now)
print('順位：')

rankin = 'no'
for i in range(100):
	if itemWord in ranking[i]:
		print(str(i + 1) + '位')
		rankin = 'yes'

if rankin == 'no':
	print('圏外')
