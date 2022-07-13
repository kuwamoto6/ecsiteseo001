from selenium import webdriver
import chromedriver_binary

driver_path = "/app/.chromedriver/bin/chromedriver"
driver = webdriver.Chrome(executable_path=driver_path)

driver.get('https://search.rakuten.co.jp/search/mall/%E3%83%80%E3%82%A4%E3%82%A8%E3%83%83%E3%83%88/')

html = driver.page_source

print(html)