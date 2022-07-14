from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome import service as fs

driver_path = '/app/.chromedriver/bin/chromedriver'
chrome_service = fs.Service(executable_path=driver_path)
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(service=chrome_service, options=options)

driver.get('https://search.rakuten.co.jp/search/mall/%E3%83%80%E3%82%A4%E3%82%A8%E3%83%83%E3%83%88/')

html = driver.page_source

print(html)