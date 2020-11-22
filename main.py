import requests
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time

driver = webdriver.Chrome(executable_path="chromedriver.exe")

url = "https://www.google.com/"
driver.get(url)

keyword = "호서대학교"

search = driver.find_element_by_class_name("gLFyf.gsfi")
search.send_keys(keyword)
search.submit()


# 뉴스 제목
driver.find_elements_by_class_name("hide-focus-ring")[2].click()
html = driver.page_source
soup = bs(html, "html.parser")
title_list = soup.find_all("div", {"class": "JheGif nDgy9d"})
for title in title_list:
    print(title.text)


driver.close()


''' 제목
html = driver.page_source
soup = bs(html, "html.parser")
title_list = soup.find_all("h3", {"class": "LC20lb DKV0Md"})
for title in title_list:
    print(title.text)
'''




