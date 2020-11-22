from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time

driver = webdriver.Chrome(executable_path="chromedriver.exe")

# 뉴스 제목
keyword = input("키워드를 입력하시오: ")


base_url = ("https://www.google.com/search?q="+keyword+"&tbm=nws&start={}")

#10, 20, 30, ...
for i in range(10):
    url = base_url.format(i*10)
    driver.get(url)
    html = driver.page_source
    soup = bs(html, "html.parser")
    title_list = soup.find_all("div", {"class": "JheGif nDgy9d"})

    for title in title_list:
        print(title.text)


driver.close()






