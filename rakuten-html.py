from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome import service as fs
from bs4 import BeautifulSoup
import time

page = 'https://search.rakuten.co.jp/search/mall/%E3%83%80%E3%82%A4%E3%82%A8%E3%83%83%E3%83%88/'
itemWord = '17日終了★クーポンで198円★サラシアブラック'

driver_path = '/app/.chromedriver/bin/chromedriver'
chrome_service = fs.Service(executable_path=driver_path)
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=chrome_service, options=options)

ranking = []
for i in range(3):
	num = i + 1
	driver.get(page + '?p=' + str(num))
	html = driver.page_source
	soup = BeautifulSoup(html, 'html.parser')
	for itemtitle in soup.find_all(class_='content title'):
		itemName = itemtitle.text
		if '[PR]' in itemName:
			continue

		ranking.append(itemName)
	time.sleep(1)

del ranking[100:]

print(ranking)

print('順位：')

rankin = 'no'
for i in range(100):
	if itemWord in ranking[i]:
		print(i + 1)
		rankin = 'yes'

if rankin == 'no':
	print('圏外')
